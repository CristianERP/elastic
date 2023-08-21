import os
import time
import requests
from datetime import datetime, timedelta

from elasticsearch_config import es

from ..helpers.filter_data import index_production
from index_constants import production

API_KEY = os.getenv("API_KEY")
index_name = production


def get_next_period():
    name_index = production
    respond = es.search(
        index=name_index, query={"match_all": {}}, sort=[{"period": "desc"}]
    )

    period = respond["hits"]["hits"][0]["_source"]["period"]
    latest_date = datetime.strptime(period, "%Y-%m")

    next_date = latest_date + timedelta(days=31)
    next_period = f"{next_date.year:04d}-{next_date.month:02d}"

    return next_period


def get_data_from_api(next_period):
    api_url = f"https://api.eia.gov/v2/petroleum/crd/crpdn/data/?frequency=monthly&data[0]=value&start={next_period}&offset=0&length=5000&api_key={API_KEY}"
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        return response.json().get("response", {}).get("data", []), response.status_code
    except requests.exceptions.RequestException:
        return [], response.status_code


def index_data_in_elasticsearch(data_list):
    filtered_data = index_production(data_list)
    for item in filtered_data:
        es.index(index=index_name, document=item)


def main():
    start_time = time.time()
    next_period = get_next_period()
    data_list, status_code = get_data_from_api(next_period)
    if status_code == 200:
        index_data_in_elasticsearch(data_list)
        end_time = time.time()
        all_time = end_time - start_time
        print(
            f"Ingesta periodo {next_period}, Tiempo: {all_time} seg., Cantidad registros : {len(data_list)}"
        )
    else:
        print(f"Error al obtener los datos. Código de estado: {status_code}")
