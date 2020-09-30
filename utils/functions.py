import cedears
from datetime import datetime
import json
# cantidad de ultimos N items a retornar por lista
items_ret = 100

#  from https://github.com/Primera-Generacion-AHK-Sistemas/flask_yahoo_finance/blob/master/app.py
"""
def get_name(ticker):

    for i in cedears.lista:
        if(i['ticker'] == ticker):
            return i['nombre']

    return 'nombre'
"""

def data_pandas_to_arrays(data_pandas):
    #print("data_pandas")
    #print(data_pandas)
    del data_pandas['ticker']

    data_json = data_pandas.to_json(orient='records')
    data_dict = json.loads(data_json)

    data_array = []

    for data in data_dict:
        data["date"] = int(data["date"])
        #data["open"] = round(data["open"], 2)
        #data["high"] = round(data["high"], 2)
        #data["low"] = round(data["low"], 2)
        #data["close"] = round(data["close"], 2)
        
        # item = [Timestamp, O, H, L, C]
        item = []
        
        item.append(data["date"])
        #item.append(data["open"])
        #item.append(data["high"])
        #item.append(data["low"])
        #item.append(data["close"])

        data_array.append(item)
    
    return data_array

# obtener el nombre del cedear buscando por ticker
def get_name(ticker):
    for i in cedears.lista:
        if(i['ticker'] == ticker):
            return i['nombre']

# devuelve un json con todos los cedears
def getCedears():
    return cedears.lista
    
# convertir fechas en formato epoch a YYYY/MM/DD
# devolver como lista
def date_converter(dates):
    str_dates = []
    for item in dates:
        item = datetime.utcfromtimestamp(item/1000000000).strftime('%Y/%m/%d')
        str_dates.append(item)

    return str_dates


# convertir serie pandas a lista
# devolver últimos items_ret
def pd_series_to_list(inputs):
    datos = {}
    for key, value in inputs.items():
        #print("inputs[key]")
        #print(inputs[key])
        inputs[key] = value.values.tolist()[-items_ret:]
        """
        if key != "date":
            inputs[key] = value.values.tolist()[-items_ret:]
            pass
        """
        
        #print(value.values)
    print(inputs)

    return inputs
