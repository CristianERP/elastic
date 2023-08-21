import os
import time
from elasticsearch_config import es
from elasticsearch import helpers

SMALL_FILE_SIZE_THRESHOLD = 500 * 1024
dsv_directory = os.getenv("DSV_DIRECTORY")

index_dsv_mapping = {
    "county": "GP_COUNTY_DATA_TABLE.dsv",
    "district": "GP_DISTRICT_DATA_TABLE.dsv",
    "og_county": "OG_COUNTY_CYCLE_DATA_TABLE.dsv",
    "og_county_lease": "OG_COUNTY_LEASE_CYCLE_DATA_TABLE.dsv",
    "og_district": "OG_DISTRICT_CYCLE_DATA_TABLE.dsv",
    "og_field": "OG_FIELD_CYCLE_DATA_TABLE.dsv",
    "og_field_data": "OG_FIELD_DW_DATA_TABLE.dsv",
    "og_operator": "OG_OPERATOR_CYCLE_DATA_TABLE.dsv",
    "og_operator_data": "OG_OPERATOR_DW_DATA_TABLE.dsv",
}


def ingestion_dsv_bulk(index_name, delimiter="}", batch_size=1000):
    filename = index_dsv_mapping[index_name]
    dsv_file_path = os.path.join(dsv_directory, filename)

    try:
        with open(dsv_file_path, "r", encoding="utf-8") as dsv_file:
            header_line = dsv_file.readline()
            field_names = header_line.strip().split(delimiter)
            data_list = [line.strip().split(delimiter) for line in dsv_file]

        bulk_data = []
        for fields in data_list:
            if len(fields) != len(field_names):
                continue
            data = dict(zip(field_names, fields))
            bulk_data.append({"_index": index_name, "_source": data})

            if len(bulk_data) >= batch_size:
                helpers.bulk(es, bulk_data)
                bulk_data = []

        if bulk_data:
            helpers.bulk(es, bulk_data)

        return len(data_list)
    except FileNotFoundError:
        return 0


def ingestion_dsv(index_name, delimiter="}"):
    filename = index_dsv_mapping[index_name]
    dsv_file_path = os.path.join(dsv_directory, filename)

    try:
        with open(dsv_file_path, "r", encoding="utf-8") as dsv_file:
            header_line = dsv_file.readline()
            field_names = header_line.strip().split(delimiter)
            data_list = [line.strip().split(delimiter) for line in dsv_file]

        for fields in data_list:
            if len(fields) != len(field_names):
                continue
            data = dict(zip(field_names, fields))
            es.index(index=index_name, document=data)

        return len(data_list)
    except FileNotFoundError:
        return 0


def main(index_name):
    print("inicio")
    start_time = time.time()
    filename = index_dsv_mapping.get(index_name)
    records = ingestion_dsv(index_name)
    # if filename:
    #     dsv_file_path = os.path.join(dsv_directory, filename)
    #     file_size = os.path.getsize(dsv_file_path)

    #     if file_size <= SMALL_FILE_SIZE_THRESHOLD:
    #         records = ingestion_dsv(index_name)
    #     else:
    #         records = ingestion_dsv_bulk(index_name)
    # else:
    #     print(f"No se encontró el archivo asociado al índice: {index_name}")
    #     records = 0

    end_time = time.time()
    all_time = end_time - start_time
    print(
        f"Ingesta full index prices, Tiempo: {all_time} seg., Cantidad registros : {records}"
    )
