from datetime import datetime
import pandas as pd
from function import *
from config import *

if __name__ == '__main__':
    # Obtener del archivo txt la key
    with open('credenciales.txt', 'r') as f:
        key = f.read()

    cityList = ["London", "New York", "Cordoba", "Taipei",
                "Buenos Aires", "Mexico City", "Dublin", "Tbilisi", "Bogota", "Tokio"]

    coordList = ["lat=31&lon=64", "lat=40&lon=-73", "lat=-31&lon=-64", "lat=25&lon=64", "lat=-34&lon=-58",
                 "lat=19&lon=-99", "lat=53&lon=6", "lat=41&lon=44", "lat=4&lon=74", "lat=35&lon=139"]

    # Realizamos la primera busqueda por nombre de la ciudad
    dataF = pd.DataFrame()
    dataF2 = pd.DataFrame()
    list=[]

    for city in cityList:
        list.append(normalize(search(city, key)))


    """ for city in [1, 2, 3]:
        list.append(normalize(dataHardcode)) """

    

    for lis in list:
      
      dataF=  pd.concat([dataF,lis], ignore_index=True)
    
    print(list)

    

    """ for coords in coordList:
        # Separamos los elementos del arrregolo en longitud y latitud
        lat, lon = coords.split('&')
    # Extraemos los valores numéricos de latitud y longitud después de "lat=" y "lon="
        lat = float(lat.split('=')[1])
        lon = float(lon.split('=')[1])
    # Realizamos la segunda busqueda por latitud y longitud de la ciudad
        result = search2(lat, lon, key)
        dataF2 = pd.concat([dataF2, normalize(result)], ignore_index=True)

    # Concatenamos los resultados obtenidos
    df = pd.concat([dataF, dataF2])

    date = datetime.now().strftime("%Y%m%d")

    # Guardamos los resultados en un csv
    df.to_csv(f"data_analytics/openweather/Archivo_{date}.csv", index=False) """

    """ result_df.to_csv(f"data_analytics/openweather/Archivo_{date}.csv", index=False) """
