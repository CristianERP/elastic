import os
import time
import requests
from datetime import datetime
from config import *
from elasticsearch_config import es

from .helpers.filter_data import index_production
from index_constants import production

API_KEY = os.getenv("API_KEY")

# Intervalos de tiempo
current_year = datetime.now().year

list_year = []

for year in range(1960, current_year, 5):
    list_year.append(year)

if current_year % 5 != 0:
    list_year.append(current_year)


def ingestion_year(start_year, end_year):
    api_url = """https://api.eia.gov/v2/petroleum/crd/crpdn/data/?frequency=monthly&data[0]=value&start={start_year}-01&end={end_year}-12&offset=0&length=5000&api_key={API_KEY}""".format(
        start_year=start_year, end_year=end_year, API_KEY=API_KEY
    )
    response = requests.get(api_url)
    data_json = response.json()

    if response.status_code == 200:
        data_json = response.json()
        data_list = data_json.get("response", {}).get("data", [])
        records = data_json.get("response", {}).get("total")
        filtered_data = index_production(data_list)

    else:
        print(f"Error al obtener los datos. Código de estado: {response.status_code}")

    index_name = production
    for item in filtered_data:
        es.index(index=index_name, document=item)

    return records


def main():
    start_year = list_year[0]
    end_year = start_year + 4

    i = 1
    while end_year <= list_year[-1] and start_year != end_year:
        start_time = time.time()
        records = ingestion_year(start_year, end_year)
        end_time = time.time()
        all_time = end_time - start_time
        print(
            f"Ingesta intervalo {start_year}-{end_year}, Tiempo: {all_time} seg., Cantidad registros : {records}"
        )
        start_year = list_year[i]
        if (start_year + 4) > current_year:
            end_year = current_year
        else:
            end_year = start_year + 4
        i += 1
