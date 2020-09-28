import json
try:
    print(json.dumps(
        {"x" : float("NaN")},
        allow_nan=True))
except ValueError as error:
    print(error)