import os
import time
from elasticsearch_config import es
from elasticsearch import helpers

from index_constants import fields

txt_file_path = os.getenv("TXT_FILE_PATH")
index_name = fields

field_lengths = [3, 8, 3, 1, 5, 32]
field_names = [
    "field-district",
    "field-number",
    "field-county-code",
    "field-multi-couties",
    "field-classification",
    "field-name",
]


def split_line(line, field_lengths, field_names):
    record = {}
    start = 0
    for index, length in enumerate(field_lengths):
        field_name = field_names[index]
        field_value = line[start : start + length].strip()
        record[field_name] = field_value
        start += length
    return record


def ingestion_fields():
    with open(txt_file_path, "r", encoding="utf-8") as txt_file:
        data = []
        for line_number, line in enumerate(txt_file, start=1):
            line = line.rstrip("\n")
            record = split_line(line, field_lengths, field_names)
            data.append(record)

    bulk_data = [{"_index": index_name, "_source": item} for item in data]
    helpers.bulk(es, bulk_data)

    return len(data)


def main():
    start_time = time.time()
    records = ingestion_fields()
    end_time = time.time()
    all_time = end_time - start_time
    print(f"Ingesta fields, Tiempo: {all_time} seg., Cantidad registros : {records}")
