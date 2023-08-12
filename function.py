import requests
from config import *


def search(city, key):
    url = f'{baseUrl}q={city}&appid={key}'

    request = requests.get(url)

    if request.status_code == 200:
        return request.json()
    else:
        raise Exception('Error searching status code', request.status_code)


def search2(lat, lon, key):
    url = f'{baseUrl}lat={lat}&lon={lon}&appid={key}&units=metric'

    request = requests.get(url)
    if request.status_code==200:
        return request.json()
    else:
        raise Exception('Error searching status code', request.status_code)