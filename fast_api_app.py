from datetime import date, timedelta
from utils import ta_calcs
from utils import functions as fnc
#from flask import Flask, request, jsonify
#from flask_cors import cross_origin
import json
from typing import Optional

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
#app = Flask(__name__)


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
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.route('/api/ta', methods=['GET'])
def get_adx():
    ticker = Request.args.get('ticker')
    indicator = Request.args.get('indicator')
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

    return json.dumps(return_json)

@app.route('/', methods=['GET'])
def get_docs():

    return_json = {}
    return_json['indicators'] = ta_calcs.get_indicators_types()
    return_json['cedears'] = fnc.getCedears()
    return json.dumps(return_json)




app = FastAPI()


import uvicorn
if __name__ == '__main__':
    # app.run(debug=True, threaded=True, port=5000)
    uvicorn.run(app)
