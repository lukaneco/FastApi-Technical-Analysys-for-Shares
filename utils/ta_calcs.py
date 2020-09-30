import yahoo_fin.stock_info as yf
import pandas_ta as ta
import pandas as pd


# cantidad de ultimos N items a retornar por lista
items_ret = 100


def get_ohlc_values(ticker, start_date):
    data = yf.get_data(ticker, start_date=start_date, index_as_date=False)
    # mm/dd/yyyy
    # get_data(ticker, start_date = None, end_date = None, index_as_date = True, interval = “1d”)
    # https://algotrading101.com/learn/yahoo-finance-api-guide/
    #print(data)

    # devolver inputs y lista de diccionarios con fecha, OHLC
    inputs = {
        'date': pd.Series(data['date']),
        'open': pd.Series(data['open']),
        'high': pd.Series(data['high']),
        'low': pd.Series(data['low']),
        'close': pd.Series(data['close']),
        'adjclose': pd.Series(data['adjclose']),
        'volume': pd.Series(data['volume'])
    }

    #print(inputs)

    return inputs
"""
def funcname(ticker, start_date):
    data = yf.get_data(ticker, start_date=start_date, index_as_date=False)

    print(data)

    # devolver inputs y lista de diccionarios con fecha, OHLC
    inputs = {
        'date': pd.Series(data['date']),
        'open': pd.Series(data['open']),
        'high': pd.Series(data['high']),
        'low': pd.Series(data['low']),
        'close': pd.Series(data['close']),
        'adjclose': pd.Series(data['adjclose']),
        'volume': pd.Series(data['volume'])
    }

    #print(inputs)
    #inputs['close'][-60:]
    return inputs['close'][-60:]
"""
def get_stoch_values(inputs):
    stoch_values = ta.stoch(inputs['high'], inputs['low'], inputs['close'])
    #print(stoch_values)

    ret_dict = {}

    ret_dict['slowk'] = stoch_values['STOCHk_5'].values.tolist()[-items_ret:]
    ret_dict['slowd'] = stoch_values['STOCHd_3'].values.tolist()[-items_ret:]

    #print(ret_dict)

    return ret_dict


def get_adx_values(inputs):
    adx_values = ta.adx(inputs['high'], inputs['low'], inputs['close'])
    #print(adx_values)

    ret_dict = {}

    ret_dict['adx'] = adx_values['ADX_14'].values.tolist()[-items_ret:]
    ret_dict['di_minus'] = adx_values['DMN_14'].values.tolist()[-items_ret:]
    ret_dict['di_plus'] = adx_values['DMP_14'].values.tolist()[-items_ret:]
    #print(ret_dict)
    return ret_dict


def get_bbands_values(inputs):
    bbands_values = ta.bbands(inputs['close'])
    #print(bbands_values)

    ret_dict = {}

    ret_dict['lower'] = bbands_values['BBL_5_2.0'].values.tolist()[-items_ret:]
    ret_dict['mid'] = bbands_values['BBM_5_2.0'].values.tolist()[-items_ret:]
    ret_dict['upper'] = bbands_values['BBU_5_2.0'].values.tolist()[-items_ret:]
    ret_dict['price'] = inputs['close'].values.tolist()[-items_ret:]

    #print(ret_dict)

    return ret_dict


def get_atx_values(inputs):
    ret_dict = {}
    ret_dict['price'] = inputs['close'].values.tolist()[-items_ret:]
    return ret_dict


def get_indicator_values(indicator, inputs):
    switcher = {
        'stoch': get_stoch_values(inputs),
        'adx': get_adx_values(inputs),
        'bbands': get_bbands_values(inputs),
        'atx': get_atx_values(inputs)
    }

    return switcher.get(indicator, "Invalid Indicator")


# lista = [{'type': 'stoch'}, {'type': 'adx'}, {'type': 'bbands'}, {'type': 'atx'}]
lista = {'stoch':['slowk','slowd'], 'adx':['adx','di_plus','di_minus'], 'bbands':['upper','mid','lower','price'], 'atx':['price']}
# lista = {'stoch':{'slowk','slowd'}, 'adx':{'adx','di_plus','di_minus'}, 'bbands':{'upper','mid','lower','price'}, 'atx':{'price'}}

def get_indicators_types():
    return lista

def get_indicators_values():
    return lista
