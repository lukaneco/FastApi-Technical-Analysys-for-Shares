from datetime import date, timedelta
from utils import ta_calcs
from utils import functions as fnc
#from flask import Flask, request, jsonify
#from flask_cors import cross_origin
import json
from typing import Optional

from fastapi import FastAPI, Request, Path, Query

from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic import BaseModel
# https://fastapi.tiangolo.com/
# https://fastapi.tiangolo.com/tutorial/s
# https://fastapi.tiangolo.com/tutorial/debugging/
app = FastAPI()



# https://fastapi.tiangolo.com/tutorial/cors/
from fastapi.middleware.cors import CORSMiddleware
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

@app.get("/items/{item_id}")
async def read_items(
    item_id: int = Path(..., title="The ID of the item to get"),
    q: Optional[str] = Query(None, alias="item-query"),
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results

from fastapi import Body, FastAPI
from pydantic import BaseModel

@app.get("/items2/")
# http://127.0.0.1:8000/items2/?item_id=1&item=qweas&user=asdasd
# https://fastapi.tiangolo.com/tutorial/body-multiple-params/#multiple-body-params-and-query
async def update_item(
    *,
    item_id: int,
    item: str,
    user: str,
    q: Optional[str] = None
):
    results = {"item_id": item_id, "item": item, "user": user}
    if q:
        results.update({"q": q})
    return results

@app.get('/api/ta')
# http://127.0.0.1:5000/api/ta?ticker=AMD&indicator=adx
# http://127.0.0.1:5000/api/ta?ticker=AMD&indicator=adx
# http://127.0.0.1:8000/api/ta/?ticker=AMD&indicator=adx
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
"""