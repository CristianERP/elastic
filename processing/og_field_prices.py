from elasticsearch_config import es
from elasticsearch.helpers import bulk
import time
import pandas as pd

new_index = "og_county_prices"
prices_wti = "prices_wti"
og_index = "og_county"

# ---------- CREAR INDEX OG FIELD PRICES ----------

og_mapp = es.indices.get_mapping(index=og_index)[og_index]

og_mapp["mappings"]["properties"]["value"] = {"type": "float"}

es.indices.create(index=new_index, body=og_mapp, ignore=400)

# ---------- CRUZAR PRECIOS POR PERIODO ----------

start_time = time.time()

query = {"query": {"match_all": {}}}

prices_wti_hits = []
og_hits = []


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


get_batch_data(prices_wti, prices_wti_hits)
get_batch_data(og_index, og_hits)


# Convertir a DataFrames
df_prices = pd.DataFrame(prices_wti_hits)
df_og_index = pd.DataFrame(og_hits)


df_final = pd.merge(
    df_og_index, df_prices, left_on="CYCLE_YEAR_MONTH", right_on="period", how="left"
)

docs = df_final.to_dict(orient="records")


def ingestion_bulk(index_name, batch_size=5000):
    data = [{"_index": index_name, "_source": doc} for doc in docs]
    len_data = len(data)

    for i in range(0, len_data, batch_size):
        success, failed = bulk(es, data[i : i + batch_size])

    if failed:
        print(f"Error al indexar {failed} documentos.")
    else:
        print(f"Se indexaron {success} documentos correctamente.")


ingestion_bulk(new_index)

end_time = time.time()
all_time = end_time - start_time

print(f"Tiempo de procesamiento: {float(all_time) / 60} minutos.")
