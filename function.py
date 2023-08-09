import requests
from config import *


def search(city, key):
    url = f'{baseUrl}q={city}&api_key={key}'
    request = requests.get(url)

    if request.status_code == 200:

        data = request.json()
        result = {
            'id_ciudad': data['id'],
            'nombre_ciudad': data['name'],
            'lon_ciudad': data['coord']['lon'],
            'lat_ciudad': data['coord']['lat'],
        }

    else:
        raise Exception('Error searching status code', request.status_code)
