import os
import time
import requests
from config import *
from datetime import datetime, timedelta
from elasticsearch_config import es

from .helpers.filter_data import index_prices
from index_constants import prices

API_KEY = os.getenv("API_KEY")


def get_next_period():
    name_index = prices
    respond = es.search(
        index=name_index, query={"match_all": {}}, sort=[{"period": "desc"}]
    )

    period = respond["hits"]["hits"][0]["_source"]["period"]
    latest_date = datetime.strptime(period, "%Y-%m")

    next_date = latest_date + timedelta(days=31)
    next_period = f"{next_date.year:04d}-{next_date.month:02d}"

    return next_period


def ingestion_next_period(next_period):
    api_url = """https://api.eia.gov/v2/petroleum/pri/spt/data/?frequency=monthly&data[0]=value&facets[product][]=EPCBRENT&facets[product][]=EPCWTI&start={next_period}&sort[0][column]=period&sort[0][direction]=desc&offset=0&length=5000&api_key={API_KEY}""".format(
        next_period=next_period, API_KEY=API_KEY
    )
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
    next_period = get_next_period()
    records = ingestion_next_period(next_period)
    end_time = time.time()
    all_time = end_time - start_time
    print(
        f"Ingesta periodo {next_period}, Tiempo: {all_time} seg., Cantidad registros : {records}"
    )
