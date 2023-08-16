import os
import time
from dbfread import DBF
from elasticsearch_config import es
from config import *
from index_constants import wells

dbf_directory = os.getenv("DBF_DIRECTORY")
index_name = wells


def load_dbf_to_elasticsearch(dbf_file):
    records = []
    count_records = 0

    for record in DBF(dbf_file, encoding="utf-8"):
        records.append(record)

    for idx, record in enumerate(records):
        es.index(index=index_name, id=idx, document=record)
        count_records = count_records + 1
    return count_records


def main():
    list_dbf_file = os.listdir(dbf_directory)
    for filename in list_dbf_file:
        if filename.endswith(".dbf"):
            dbf_file_path = os.path.join(dbf_directory, filename)
            start_time = time.time()
            records = load_dbf_to_elasticsearch(dbf_file_path)
            end_time = time.time()
            all_time = end_time - start_time
            print(
                f"Archivo cargado {filename}, Tiempo: {all_time} seg., Cantidad registros : {records}"
            )
