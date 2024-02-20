import os
import pandas as pd
from shapely.geometry import Point, Polygon
from elasticsearch_config import es
from elasticsearch.helpers import bulk
from multiprocessing import Process, Manager
import time

start_time = time.time()

# ---------- CREAR INDEX OG FIELD PRICES ----------

og_mapp = es.indices.get_mapping(index="wells_coordinates_texas")[
    "wells_coordinates_texas"
]

og_mapp["mappings"]["properties"]["geology_type"] = {
    "type": "text",
    "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
}


es.indices.create(index="well_geology", body=og_mapp, ignore=400)

# ---------- IDENTIFICAR TIPO DE GEOLOGIA ----------

geology_index = "tx_geol_poly"
well = "wells_coordinates_texas"
query = {"query": {"match_all": {}}}
index_geology_hits = []
well_hits = []


def get_batch_data(index, data):
    res = es.search(index=index, body=query, size=10000, scroll="2m")
    scroll_id = res["_scroll_id"]
    hits = res["hits"]["hits"]
    data.extend(hit["_source"] for hit in hits)

    while len(hits) > 0:
        res = es.scroll(scroll_id=scroll_id, scroll="2m")
        scroll_id = res["_scroll_id"]
        hits = res["hits"]["hits"]
        data.extend(hit["_source"] for hit in hits)


def process_geology_hits():
    get_batch_data(geology_index, index_geology_hits)
    polygons = []

    for hit in index_geology_hits:
        coordinates = hit["geometry"]["coordinates"][0]
        polygons.append(Polygon(coordinates))

    return polygons


def process_well_hit(well_hit, polygons, index_geology_hits, result):
    well_location = Point(*well_hit["geometry"])
    for i, polygon in enumerate(polygons):
        if well_location.within(polygon):
            well_hit["geology_type"] = index_geology_hits[i]["GENERALIZE"]
    result.append(well_hit)


def process_well_hits(well_hits, polygons, index_geology_hits, result):
    for well_hit in well_hits:
        process_well_hit(well_hit, polygons, index_geology_hits, result)


if __name__ == "__main__":
    manager = Manager()
    result = manager.list()

    get_batch_data(well, well_hits)
    polygons = process_geology_hits()

    chunk_size = max(len(well_hits) // 10, 1)
    processes = []

    for i in range(0, len(well_hits), chunk_size):
        process = Process(
            target=process_well_hits,
            args=(well_hits[i : i + chunk_size], polygons, index_geology_hits, result),
        )
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    def ingestion_bulk(index_name, batch_size=5000):
        data = [{"_index": index_name, "_source": doc} for doc in result]
        len_data = len(data)

        for i in range(0, len_data, batch_size):
            success, failed = bulk(es, data[i : i + batch_size])

        if failed:
            print(f"Error al indexar {failed} documentos.")
        else:
            print(f"Se indexaron los documentos correctamente.")

    ingestion_bulk("well_geology")

    end_time = time.time()
    all_time = end_time - start_time

    print(f"Tiempo de procesamiento: {float(all_time) / 60} minutos.")
