from datetime import datetime
import pandas as pd
from pandas import json_normalize
import json
from function import *
from config import *
if __name__ == '__main__':
    # Obtener del archivo txt la key
    with open('credenciales.txt', 'r') as f:
        key = f.read()

    cityList = ["London", "New York", "Cordoba", "Taipei",
                "Buenos Aires", "Mexico DF", "Dublin", "Tilfis", "Bogota", "Tokio"]

    coordList = ["lat=31&lon=64", "lat=40&lon=-73", "lat=-31&lon=-64", "lat=25&lon=64", "lat=-34&lon=-58",
                 "lat=19&lon=-99", "lat=53&lon=6", "lat=41&lon=44", "lat=4&lon=74", "lat=35&lon=139"]

    coords_list = []
    # Separamos los elementos del arrregolo en longitud y latitud
    for coords in coordList:
        lat, lon = coords.split('&')

    # Extraemos los valores numéricos de latitud y longitud después de "lat=" y "lon="
        lat = float(lat.split('=')[1])
        lon = float(lon.split('=')[1])

    # Creamos un diccionario con las coordenadas en formato adecuado y lo agregamos a la lista
        coords_dict = [lat, lon]
        coords_list.append(coords_dict)

    # Realizamos la primera busqueda por nombre de la ciudad
    for city in cityList:
        respuesta = search(city, key)
        dataF = pd.DataFrame.from_dict(json_normalize(respuesta))

    """ normalizado = json_normalize(dataHardcode)
    dataF = pd.DataFrame.from_dict(normalizado)
    dataF = dataF.assign(City='Londes') """

    for coords_list in coords:
        respuesta = search2(coords[0], coords[1], key)
        dataF2 = pd.DataFrame.from_dict(json_normalize(respuesta))

    df_todas_ciudades = pd.concat([dataF, dataF2])
