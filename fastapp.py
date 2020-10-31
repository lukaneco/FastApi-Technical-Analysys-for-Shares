from datetime import date, timedelta
from utils import ta_calcs
from utils import functions as fnc
#from flask import Flask, request, jsonify
#from flask_cors import cross_origin
import json

from typing import Optional
import typing

from fastapi import FastAPI, Request, Path, Query,Body
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel
# https://fastapi.tiangolo.com/
# https://fastapi.tiangolo.com/tutorial/s
# https://fastapi.tiangolo.com/tutorial/debugging/


app = FastAPI()

import orjson, datetime, numpy

class ORJSONResponse(JSONResponse):
    media_type = "application/json"

    def render(self, content: typing.Any) -> bytes:
        return orjson.dumps(content,
        allow_nan=True)

tags_metadata = [
    {
        "name": "users",
        "description": "Operations with users. The **login** logic is also here.",
    },
    {
        "name": "items",
        "description": "Manage items. So _fancy_ they have their own docs.",
        "externalDocs": {
            "description": "Items external docs",
            "url": "https://fastapi.tiangolo.com/",
        },
    },
]


app = FastAPI(
    title="Fast Api Technical Analysys for Shares",
    description="This is a very fancy project, with auto docs for the API and everything",
    version="0.5.0",
    openapi_tags=tags_metadata,
    # default_response_class=ORJSONResponse
)

# https://fastapi.tiangolo.com/tutorial/cors/
origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://127.0.0.1:8000",
    "http://localhost:8080",
    "http://127.0.0.1:8080",
    "http://127.0.0.1:5500",
    "http://127.0.0.1:5501",
    "http://localhost:4200",
    "http://argenshares.herokuapp.com",
    "https://argenshares.herokuapp.com"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)



# https://fastapi.tiangolo.com/tutorial/metadata/
@app.get('/api/ta', tags=["old"])
# http://127.0.0.1:8000/api/ta/?ticker=AMD&indicator=adx
# https://fastapi.tiangolo.com/tutorial/body-multiple-params/#multiple-body-params-and-query
async def get_something_old(
    *,
    ticker: str,
    indicator: str,
    q: Optional[str] = None
):
    print(f"indicator: {indicator}, ticker: {ticker}")

    # date params format: YYYY/MM/DD
    start_date = date.today() - timedelta(days=365)
    start_date = start_date.strftime("%Y/%m/%d")

    talib_inputs = ta_calcs.get_ohlc_values(ticker, start_date)

    indicator_values = ta_calcs.get_indicator_values(indicator, talib_inputs)

    talib_inputs = fnc.pd_series_to_list(talib_inputs)

    str_dates = fnc.date_converter(talib_inputs['date'])

    if q:
        print({"q": q})


    return_json = {}
    return_json['ticker'] = ticker
    return_json['name'] = fnc.get_name(ticker)
    return_json[f'{indicator}'] = indicator_values
    return_json['date'] = str_dates

    # return_json['date'] = str_dates

    # return json.dumps(return_json)
    json_compatible_item_data = jsonable_encoder(return_json)
    return JSONResponse(content=json_compatible_item_data)


# https://fastapi.tiangolo.com/tutorial/metadata/
@app.get('/api', tags=["prod"])
# http://127.0.0.1:8000/api/ta/?ticker=AMD&indicator=adx
# https://fastapi.tiangolo.com/tutorial/body-multiple-params/#multiple-body-params-and-query
async def get_something(
    *,
    ticker: str,
    indicator: str,
    date_old: str,
    date_new: str,
    #q: Optional[str] = None
):
    #print(f"indicator: {indicator}, ticker: {ticker}")

    # date params format: YYYY/MM/DD
    start_date = date.today() - timedelta(days=365)
    #start_date = start_date.strftime("%Y/%m/%d")
    start_date = start_date.strftime("%m/%d/%Y")
    #print("start_date")
    #print(start_date)

    talib_inputs = ta_calcs.get_ohlc_values(ticker, start_date)

    indicator_values = ta_calcs.get_indicator_values(indicator, talib_inputs)

    talib_inputs = fnc.pd_series_to_list(talib_inputs)

    print(type(talib_inputs))
    # talib_inputs['price'] = indicator_values['price']

    return_json = {}
    return_json['ticker'] = ticker
    return_json['name'] = fnc.get_name(ticker)
    return_json['indicator'] = indicator
    return_json['values'] = ta_calcs.lista[indicator]
    # candlestick
    #return_json['data'] = talib_inputs
    return_json['data']= indicator_values

    # return_json[f'{indicator}'] = indicator_values
    return_json['date'] = fnc.date_converter(talib_inputs['date'])
    talib_inputs.pop("date")
    # return_json['date'] = str_dates

    # return json.dumps(return_json)
    if q:
        return_json.update({"q": q})
    json_compatible_item_data = jsonable_encoder(return_json)
    return JSONResponse(content=json_compatible_item_data)

# https://fastapi.tiangolo.com/tutorial/metadata/
@app.get('/demo', tags=["prod"])
# http://127.0.0.1:8000/api/ta/?ticker=AMD&indicator=adx
# https://fastapi.tiangolo.com/tutorial/body-multiple-params/#multiple-body-params-and-query
async def get_something_dev(
    *,
    ticker: str,
    indicator: str
):
    # json_data = ''''''
    def getFileContent(file_path):
        """
        with open(file_path, "rb") as file_content:
            return file_content
        """
        f = open(file_path, "r")
        #print(f.read())
        return f.read()
    #json_data = getFileContent("json_static.json")
    #print(gg)

    #print(f"indicator: {indicator}, ticker: {ticker}")

    if q:
        print(f"q: {q}")

    # json_data = '{"indicator":{indicator},"ticker":{ticker}}'
    import json 
  
    # Opening JSON file 
    jsonfile = open("json_static.json") 
    
    # returns JSON object as  
    # a dictionary 
    data = json.load(jsonfile) 

    # json_data = json.loads("json_static.json")
    json_compatible_item_data = jsonable_encoder(data)
    # json_compatible_item_data = json.dumps(json_data)
    return JSONResponse(content=json_compatible_item_data)
    #return json_compatible_item_data

# https://fastapi.tiangolo.com/tutorial/metadata/
# Gráfico de velas (Candlestick chart)
# http://127.0.0.1:8000/api/chart/candlestick?ticker=AMD
@app.get('/api/chart/candlestick', tags=["Candlestick"])
# http://127.0.0.1:8000/api/ta/?ticker=AMD&indicator=adx
# https://fastapi.tiangolo.com/tutorial/body-multiple-params/#multiple-body-params-and-query
async def get_data_candlestick(
    *,
    ticker: str
):
    #print(f"ticker: {ticker}")

    # date params format: YYYY/MM/DD
    start_date = date.today() - timedelta(days=365)
    #start_date = start_date.strftime("%Y/%m/%d")
    start_date = start_date.strftime("%m/%d/%Y")
    #start_date = start_date.strftime("%mm/%dd/%yyyy")
    #print(f"start_date: {start_date}")

    talib_inputs = ta_calcs.get_ohlc_values(ticker, start_date)

    talib_inputs = fnc.pd_series_to_list(talib_inputs)

    # return_json = {}

    # return json.dumps(return_json)
    #print(talib_inputs)
    json_compatible_item_data = jsonable_encoder(talib_inputs)
    # json_compatible_item_data = json.dumps(talib_inputs)
    return JSONResponse(content=json_compatible_item_data)


    
@app.get('/data')
def get_docs():
    return_json = {}
    return_json['indicators'] = ta_calcs.get_indicators_types()
    return_json['cedears'] = fnc.getCedears()
    # https://fastapi.tiangolo.com/advanced/response-directly/
    json_compatible_item_data = jsonable_encoder(return_json)
    return JSONResponse(content=json_compatible_item_data)

@app.get("/")
async def main():
    return {"message": "Hello World"}
@app.get('/ping')
def get_ping():
    return_json = {}
    return_json['pong'] = True
    return json.dumps(return_json)
"""
import uvicorn
if __name__ == '__main__':
    # app.run(debug=True, threaded=True, port=5000)
    uvicorn.run(app)
"""


# https://amitness.com/2020/06/fastapi-vs-flask/
"""
uvicorn app:app --reload

uvicorn fast_api_app:app --reload
uvicorn <app_name>:app --reload
uvicorn fastapp:app --reload
uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"
sudo python3 -m  uvicorn fastapp:app  --reload --port 80 --host 0.0.0.0
based on
https://render.githubusercontent.com/view/ipynb?commit=700633386663e8f5ffba80f65d27e41e0545658c&enc_url=68747470733a2f2f7261772e67697468756275736572636f6e74656e742e636f6d2f746f6d61736d6572656e63696f2f416e616c697369735465636e69636f416363696f6e65732f373030363333333836363633653866356666626138306636356432376534316530353435363538632f416e616c697369735465636e69636f416363696f6e65732e6970796e62&nwo=tomasmerencio%2FAnalisisTecnicoAcciones&path=AnalisisTecnicoAcciones.ipynb&repository_id=290331654&repository_type=Repository#Gr%C3%A1ficos-de-indicadores-con-matplotlib
"""