from datetime import datetime
import pandas as pd
from function import *



if __name__ == '__main__':
    # Obtener del archivo txt la key
    with open('credenciales.txt', 'r') as f:
        key = f.read()

    cityList = ["London", "New York", "Cordoba", "Taipei",
                "Buenos Aires", "Mexico City", "Dublin", "Tbilisi", "Bogota", "Tokio"]

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
    cont = 0
    for city in cityList:
        result = search(city, key)
        cont = cont + 1
        dataF = normalize(result, cont)
        


    """ datecols = ['dt', 'sunrise', 'sunset']
    nWeather = json_normalize(dataHardcode['weather'])
    nCoord = json_normalize(dataHardcode['coord'])
    nMain = json_normalize(dataHardcode['main'])
    nWind = json_normalize(dataHardcode['wind'])
    nClouds = json_normalize(dataHardcode['clouds'])
    nSys = json_normalize(dataHardcode['sys'])

    start = json_normalize({'id': dataHardcode['id'], 'name': dataHardcode['name'],
                            'cod': dataHardcode['cod'], 'dt': dataHardcode['dt']})

    result_df = pd.concat(
        [start, nWeather, nCoord, nMain, nWind, nClouds, nSys], axis=1)

    result_df[datecols] = result_df[datecols].apply(
        lambda x: pd.to_datetime(x, unit='s')) """

 # Realizamos la segunda busqueda por latitud y longitud de la ciudad
    
    for coords in coords_list:
        result = search2(coords[0], coords[1], key)
        cont = cont+1
        dataF2 = normalize(result, cont)

    df = pd.concat([dataF, dataF2])

    date = datetime.now().strftime("%Y%m%d")

    df.to_csv(f"data_analytics/openweather/Archivo_{date}.csv", index=False) 

    """ result_df.to_csv(f"data_analytics/openweather/Archivo_{date}.csv", index=False) """
