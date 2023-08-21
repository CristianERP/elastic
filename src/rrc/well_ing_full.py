import os
import time
from dbfread import DBF
from elasticsearch_config import es
from elasticsearch import helpers

from index_constants import wells

dbf_directory = os.getenv("DBF_DIRECTORY")
index_name = wells


def ingestion_dbf(dbf_file):
    data_list = []

    for record in DBF(dbf_file, encoding="utf-8"):
        data_list.append(record)

    bulk_data = [{"_index": index_name, "_source": item} for item in data_list]
    helpers.bulk(es, bulk_data)

    return len(data_list)


def main():
    list_dbf_file = os.listdir(dbf_directory)
    for filename in list_dbf_file:
        if filename.endswith(".dbf"):
            dbf_file_path = os.path.join(dbf_directory, filename)
            start_time = time.time()
            records = ingestion_dbf(dbf_file_path)
            end_time = time.time()
            all_time = end_time - start_time
            print(
                f"Archivo cargado {filename}, Tiempo: {all_time} seg., Cantidad registros : {records}"
            )
