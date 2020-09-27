from datetime import date, timedelta
from utils import ta_calcs
from utils import functions as fnc
#from flask import Flask, request, jsonify
#from flask_cors import cross_origin
import json

from typing import Optional

from fastapi import FastAPI, Request, Path, Query,Body
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel
# https://fastapi.tiangolo.com/
# https://fastapi.tiangolo.com/tutorial/s
# https://fastapi.tiangolo.com/tutorial/debugging/
app = FastAPI()



# https://fastapi.tiangolo.com/tutorial/cors/
origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://127.0.0.1:8000",
    "http://localhost:8080",
    "http://127.0.0.1:8080"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)




@app.get('/api/ta')
# http://127.0.0.1:8000/api/ta/?ticker=AMD&indicator=adx
# https://fastapi.tiangolo.com/tutorial/body-multiple-params/#multiple-body-params-and-query
async def get_something(
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

    return_json = {}
    return_json['ticker'] = ticker
    return_json['name'] = fnc.get_name(ticker)
    return_json[f'{indicator}'] = indicator_values
    return_json['date'] = str_dates

    # return json.dumps(return_json)
    if q:
        return_json.update({"q": q})
    json_compatible_item_data = jsonable_encoder(return_json)
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

based on
https://render.githubusercontent.com/view/ipynb?commit=700633386663e8f5ffba80f65d27e41e0545658c&enc_url=68747470733a2f2f7261772e67697468756275736572636f6e74656e742e636f6d2f746f6d61736d6572656e63696f2f416e616c697369735465636e69636f416363696f6e65732f373030363333333836363633653866356666626138306636356432376534316530353435363538632f416e616c697369735465636e69636f416363696f6e65732e6970796e62&nwo=tomasmerencio%2FAnalisisTecnicoAcciones&path=AnalisisTecnicoAcciones.ipynb&repository_id=290331654&repository_type=Repository#Gr%C3%A1ficos-de-indicadores-con-matplotlib
"""