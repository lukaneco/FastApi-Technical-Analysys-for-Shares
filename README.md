# FastApi Technical Analysys for actions

to use it:

```
python -m pip install -r .\requirements.txt

uvicorn fastapp:app --reload
```
and open in the browser
http://127.0.0.1:8000/api/ta/?ticker=AMD&indicator=adx

to see the options go to
http://127.0.0.1:8000/docs

based on:

  repo:
    https://github.com/tomasmerencio/flask_technical_analysys
    
  the library:
    pandas-ta
        https://github.com/twopirllc/pandas-ta

  notebook
      https://github.com/tomasmerencio/AnalisisTecnicoAcciones/blob/master/AnalisisTecnicoAcciones.ipynb



## Indicador Estocástico
-   STOCH
    - slowd
      - green
    - slowk
      - red

<p align="center">
  <img src="images/Indicador Estocástico.png" height="200" width="auto" alt="accessibility text">
</p>

### stoch response example
```
{
    "ticker": "AMD",
    "name": "Advanced Micro Devices, Inc.",
    "stoch": {
        "slowk": [
            56.17958316229338,
            42.346524809907336,
            29.51225012105018,
            21.038477801739365,
            22.321968277630805,
            22.909846238295735,
            29.687817968412766,
            27.388327999490865,
            30.68981639929022,
            31.24241433203744,
            36.949306642880984,
            40.65934283501407,
            40.30433055589724,
            40.61281581158074,
            54.30594367601368
        ],
        "slowd": [
            61.31325194047465,
            53.43169105954146,
            42.67945269775044,
            30.965750910899104,
            24.290898733473593,
            22.09009743922211,
            24.973210828113242,
            26.6619974020666,
            29.255320789064758,
            29.773519576939652,
            32.960512458069694,
            36.283687936644306,
            39.3043266779309,
            40.52549640083082,
            45.07436334783068
        ]
    },
    "date": [
        "2020/09/04",
        "2020/09/08",
        "2020/09/09",
        "2020/09/10",
        "2020/09/11",
        "2020/09/14",
        "2020/09/15",
        "2020/09/16",
        "2020/09/17",
        "2020/09/18",
        "2020/09/21",
        "2020/09/22",
        "2020/09/23",
        "2020/09/24",
        "2020/09/25"
    ]
}
```


## Índice de movimiento direccional (DMI)
-   ADX
    - ADX
      - purple
    - DI+
      - green
    - DI-
      - red


<p align="center">
  <img src="images/Índice de movimiento direccional.png" height="200" width="auto" alt="accessibility text">
</p>



### adx response example
```
{
    "ticker": "AMD",
    "name": "Advanced Micro Devices, Inc.",
    "adx": {
        "adx": [
            32.97557365713845,
            31.13920107718687,
            29.28301260635888,
            27.78285248142239,
            27.152830339354804,
            26.56780978284781,
            25.53555876356091,
            24.57703996556616,
            24.275404683811363,
            23.71893387022859,
            22.990737314250698,
            22.016000961383085,
            21.392842841784066,
            20.948616025587764,
            20.140903632196412
        ],
        "di_minus": [
            28.834084988743214,
            26.900995821779375,
            25.199580383834917,
            24.62888401812982,
            28.125706458006636,
            26.902830819045768,
            24.915881489345583,
            23.54972649454573,
            26.676259546947147,
            24.98037905037576,
            23.149919029564035,
            21.68104419822791,
            21.964222829020045,
            21.421451023996024,
            20.024651616773834
        ],
        "di_plus": [
            24.927570117929324,
            23.25638076780731,
            22.729979213363656,
            20.86189626902428,
            19.159272112539274,
            18.326247450149793,
            19.530612658983372,
            18.459735674479294,
            17.65334669752068,
            17.909982862212942,
            17.6342003411184,
            17.975378075262928,
            16.810384425536235,
            15.777070960281268,
            16.503137917619693
        ]
    },
    "date": [
        "2020/09/04",
        "2020/09/08",
        "2020/09/09",
        "2020/09/10",
        "2020/09/11",
        "2020/09/14",
        "2020/09/15",
        "2020/09/16",
        "2020/09/17",
        "2020/09/18",
        "2020/09/21",
        "2020/09/22",
        "2020/09/23",
        "2020/09/24",
        "2020/09/25"
    ]
}
```



## Bollinger Bands
-   BBANDS
    - upperband
      - green
    - middleband
      - lightblue
    - lowerband
      - yellow
    - price
      - blue


<p align="center">
  <img src="images\Bollinger Bands.png" height="200" width="auto" alt="accessibility text">
</p>

### bbands response example
```
{
    "ticker": "AMD",
    "name": "Advanced Micro Devices, Inc.",
    "bbands": {
        "lower": [
            77.80462679912686,
            73.57262831420282,
            74.5266690413792,
            77.1538215002322,
            74.79190493490863,
            74.69315889258966,
            74.73986164746434,
            75.2915169442867,
            75.06066334395571,
            73.97113598892352,
            73.96696007062658,
            74.37295345498278,
            73.36510708657012,
            73.19201954733003,
            73.8616926829115
        ],
        "mid": [
            87.55400085449219,
            85.1280014038086,
            83.07400207519531,
            80.82600250244141,
            79.58600158691407,
            78.76400146484374,
            78.81200103759765,
            77.76200103759766,
            77.2760009765625,
            76.99400177001954,
            77.002001953125,
            76.75600128173828,
            76.37000122070313,
            76.2240005493164,
            76.85
        ],
        "upper": [
            97.30337490985751,
            96.68337449341438,
            91.62133510901143,
            84.49818350465063,
            84.3800982389195,
            82.83484403709782,
            82.88414042773097,
            80.23248513090861,
            79.49133860916929,
            80.01686755111555,
            80.03704383562342,
            79.13904910849378,
            79.37489535483614,
            79.25598155130277,
            79.83830731708849
        ]
    },
    "date": [
        "2020/09/04",
        "2020/09/08",
        "2020/09/09",
        "2020/09/10",
        "2020/09/11",
        "2020/09/14",
        "2020/09/15",
        "2020/09/16",
        "2020/09/17",
        "2020/09/18",
        "2020/09/21",
        "2020/09/22",
        "2020/09/23",
        "2020/09/24",
        "2020/09/25"
    ]
}
```




## Average True Range (ATR)
-   ATR
    - price
      - yellow


<p align="center">
  <img src="images/Average True Range.png" height="200" width="auto" alt="accessibility text">
</p>
