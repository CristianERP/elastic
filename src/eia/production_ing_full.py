import os
import time
import requests
from datetime import datetime

from elasticsearch_config import es
from elasticsearch import helpers

from ..helpers.filter_data import index_production
from index_constants import production

API_KEY = os.getenv("API_KEY")
index_name = production


def get_data_from_api(start_date, end_date):
    api_url = f"https://api.eia.gov/v2/petroleum/crd/crpdn/data/?frequency=monthly&data[0]=value&start={start_date}&end={end_date}&offset=0&length=5000&api_key={API_KEY}"
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Lanza una excepción si el código de estado no es 200
        return response.json().get("response", {}).get("data", []), response.status_code
    except requests.exceptions.RequestException:
        return [], response.status_code


def index_data_in_elasticsearch(data_list):
    filtered_data = index_production(data_list)
    bulk_data = [{"_index": index_name, "_source": item} for item in filtered_data]
    helpers.bulk(es, bulk_data)


def main():
    current_year = datetime.now().year
    list_year = []

    for year in range(1960, current_year, 5):
        list_year.append(year)

    if current_year % 5 != 0:
        list_year.append(current_year)

    start_year = list_year[0]
    end_year = start_year + 4

    i = 1
    while end_year <= list_year[-1] and start_year != end_year:
        start_time = time.time()
        data_list, status_code = get_data_from_api(start_year, end_year)
        if status_code == 200:
            index_data_in_elasticsearch(data_list)
            end_time = time.time()
            all_time = end_time - start_time
            print(
                f"Ingesta intervalo {start_year}-{end_year}, Tiempo: {all_time} seg., Cantidad registros : {len(data_list)}"
            )
        else:
            print(f"Error al obtener los datos. Código de estado: {status_code}")
            break

        start_year = list_year[i]
        if (start_year + 4) > current_year:
            end_year = current_year
        else:
            end_year = start_year + 4
        i += 1
