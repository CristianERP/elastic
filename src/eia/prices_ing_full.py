import os
import requests
import time

from elasticsearch_config import es

from ..helpers.filter_data import index_prices
from index_constants import prices

API_KEY = os.getenv("API_KEY")
API_URL = f"https://api.eia.gov/v2/petroleum/pri/spt/data/?frequency=monthly&data[0]=value&facets[product][]=EPCBRENT&facets[product][]=EPCWTI&sort[0][column]=period&sort[0][direction]=desc&offset=0&length=5000&api_key={API_KEY}"
index_name = prices


def get_data_from_api():
    try:
        response = requests.get(API_URL)
        response.raise_for_status()  # Lanza una excepción si el código de estado no es 200
        return response.json().get("response", {}).get("data", []), response.status_code
    except requests.exceptions.RequestException:
        return [], response.status_code


def index_data_in_elasticsearch(data_list):
    filtered_data = index_prices(data_list)
    for item in filtered_data:
        es.index(index=index_name, document=item)


def main():
    start_time = time.time()
    data_list, status_code = get_data_from_api()
    if status_code == 200:
        index_data_in_elasticsearch(data_list)
        end_time = time.time()
        all_time = end_time - start_time
        print(
            f"Ingesta full index prices, Tiempo: {all_time} seg., Cantidad registros: {len(data_list)}"
        )
    else:
        print(f"Error al obtener los datos. Código de estado: {status_code}")
