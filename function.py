import requests
from config import *
from datetime import datetime
import pandas as pd
from pandas import json_normalize


def search(city, key):
    # Consulta a la appi
    url = f'{baseUrl}q={city}&appid={key}'

    request = requests.get(url)

    if request.status_code == 200:
        return request.json()
    else:
        raise Exception('Error searching status code', request.status_code)


def search2(lat, lon, key):
    # Consulta a la appi
    url = f'{baseUrl}lat={lat}&lon={lon}&appid={key}&units=metric'

    request = requests.get(url)

    if request.status_code == 200:
        return request.json()
    else:
        raise Exception('Error searching status code', request.status_code)


def normalize(request, cont):
    # Normalizacion de la respuesta de la api
    datecols = ['dt', 'sunrise', 'sunset']
    weather = json_normalize(request['weather'])
    coord = json_normalize(request['coord'])
    main = json_normalize(request['main'])
    wind = json_normalize(request['wind'])
    clouds = json_normalize(request['clouds'])
    sys = json_normalize(request['sys'])

    start = json_normalize({'id': request['id'], 'name': request['name'],
                            'cod': request['cod'], 'dt': request['dt']})

    result_df = pd.concat(
        [start, weather, coord, main, wind, clouds, sys], axis=cont)

    result_df[datecols] = result_df[datecols].apply(
        lambda x: pd.to_datetime(x, unit='s'))
    
    return result_df
