def index_production(data_list):
    filtered_data = []
    for item in data_list:
        filtered_item = {
            "period": item.get("period"),
            "area-name": item.get("area-name"),
            "product": item.get("product"),
            "product-name": item.get("product-name"),
            "process": item.get("process"),
            "process-name": item.get("process-name"),
            "series-description": item.get("series-description"),
            "value": item.get("value"),
            "units": item.get("units"),
        }
        filtered_data.append(filtered_item)

    return filtered_data


def index_prices(data_list):
    filtered_data = []
    for item in data_list:
        filtered_item = {
            "period": item.get("period"),
            "product": item.get("product"),
            "product-name": item.get("product-name"),
            "value": item.get("value"),
            "units": item.get("units"),
        }
        filtered_data.append(filtered_item)

    return filtered_data
