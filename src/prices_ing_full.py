import os
import requests
import time
from config import *
from elasticsearch_config import es

from .helpers.filter_data import index_prices
from index_constants import prices

API_KEY = os.getenv("API_KEY")


def ingestion_prices_full():
    api_url = f"https://api.eia.gov/v2/petroleum/pri/spt/data/?frequency=monthly&data[0]=value&facets[product][]=EPCBRENT&facets[product][]=EPCWTI&sort[0][column]=period&sort[0][direction]=desc&offset=0&length=5000&api_key={API_KEY}"
    response = requests.get(api_url)

    data_json = response.json()

    if response.status_code == 200:
        data_json = response.json()
        data_list = data_json.get("response", {}).get("data", [])
        records = data_json.get("response", {}).get("total")
        filtered_data = index_prices(data_list)
    else:
        print(f"Error al obtener los datos. Código de estado: {response.status_code}")

    index_name = prices
    for item in filtered_data:
        es.index(index=index_name, document=item)

    return records


def main():
    start_time = time.time()
    records = ingestion_prices_full()
    end_time = time.time()
    all_time = end_time - start_time
    print(
        f"Ingesta full index prices, Tiempo: {all_time} seg., Cantidad registros : {records}"
    )
