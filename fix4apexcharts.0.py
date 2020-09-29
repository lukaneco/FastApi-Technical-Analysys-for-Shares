import json

def data_pandas_to_arrays(data_pandas):
    del data_pandas['ticker']

    data_json = data_pandas.to_json(orient='records')
    data_dict = json.loads(data_json)

    data_array = []

    for data in data_dict:
        data["date"] = int(data["date"])
        data["open"] = round(data["open"], 2)
        data["high"] = round(data["high"], 2)
        data["low"] = round(data["low"], 2)
        data["close"] = round(data["close"], 2)
        
        # item = [Timestamp, O, H, L, C]
        item = []
        
        item.append(data["date"])
        item.append(data["open"])
        item.append(data["high"])
        item.append(data["low"])
        item.append(data["close"])

        data_array.append(item)
    
    return data_array



some_list = ["stoch","adx","bbands","atx"]

some_field= "stoch"

result = """
{
    "ticker": "AMD",
    "name": "Advanced Micro Devices, Inc.",
    "atx": {
        "price": [
            51.95000076293945,
            53.189998626708984
        ]
    },
    "date": [
        "2020/05/07",
        "2020/05/08"
    ]
}

"""
"""
{
    "data": [
        [
            1597622400000,
            [
                209.6,
                211.19,
                208.92,
                210.28
            ]
        ],
        [
            1597708800000,
            [
                210.53,
                212.36,
                209.21,
                211.49
            ]
        ]
    ],
    "name": "Microsoft Corporation",
    "ticker": "MSFT"
}


{
    "data": [
        [
            1597622400000,[209.6,211.19,208.92,210.28]
        ],
        [
            1597708800000,[210.53,212.36,209.21,211.49]]
        ],
    "name": "Microsoft Corporation",
    "ticker": "MSFT"
}

{
    "data": [
        [
            1597622400000,[209.6,211.19,208.92,210.28]
        ],
        [
            1597708800000,[210.53,212.36,209.21,211.49]]
        ],
    "name": "Microsoft Corporation",
    "ticker": "MSFT"
}

    "atx": {
        "price": [
            51.95000076293945,
            53.189998626708984
        ]
    },
    "date": [
        "2020/05/07",
        "2020/05/08"
    ]
"""
d=json.loads(result)
def checkJson(jsonContents):
    """
    bodyFlag = True if "body" in jsonContents["name"]
    
     and jsonContents["objects"][0]["data"]["body"] == "Present" else False
    """
    #if "body" in jsonContents["name"]:
    """
    for key, value in jsonContents.items():
        print(key, value)
    """

    if "atx" in jsonContents:
        for masteritem in jsonContents["atx"].items():
            print("some master item")
            for miniitem in masteritem:
                print("some mini item")
                print(miniitem)
                if type(miniitem) == str:
                    print("nothing")
                    pass
                else:
                    for nanoitem in miniitem:
                        print("some nano item")
                        print(nanoitem)
                        pass
                    pass
                pass
            pass
        return "KPO"
    else:
        return "NO KPO"  
    """
    if jsonContents in some_list:
        print(jsonContents)
        return "GG"
    else:
        print(jsonContents)
        return "NO GG"  
    """ 


print(checkJson(d))

"""

{
    "ticker": "AMD",
    "name": "Advanced Micro Devices, Inc.",
    "atx": {
        "price": [
            51.95000076293945,
            53.189998626708984
        ]
    },
    "date": [
        "2020/05/07",
        "2020/05/08"
    ]
}

"""
"""
if some_field in some_list:
    print(some_field)
"""

"""
def data_pandas_to_arrays(data_pandas):
    del data_pandas['ticker']

    data_json = data_pandas.to_json(orient='records')
    data_dict = json.loads(data_json)

    data_array = []

    for data in data_dict:
        data["date"] = int(data["date"])
        data["open"] = round(data["open"], 2)
        data["high"] = round(data["high"], 2)
        data["low"] = round(data["low"], 2)
        data["close"] = round(data["close"], 2)
        
        # item = [Timestamp, O, H, L, C]
        item = []
        
        item.append(data["date"])
        item.append(data["open"])
        item.append(data["high"])
        item.append(data["low"])
        item.append(data["close"])

        data_array.append(item)
    
    return data_array
"""