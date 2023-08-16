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

    dataF = pd.DataFrame()
    dataF2 = pd.DataFrame()
    list = []
    cont = 0

    # Realizamos la primera busqueda por nombre de la ciudad
    for city in cityList:
        list.append(search(city,key))
        
    for coords in coordList:
        # Separamos los elementos del arrregolo en longitud y latitud
        lat, lon = coords.split('&')
    # Extraemos los valores numéricos de latitud y longitud después de "lat=" y "lon="
        lat = float(lat.split('=')[1])
        lon = float(lon.split('=')[1])
    # Realizamos la segunda busqueda por latitud y longitud de la ciudad
        cont = cont+1
        list.append(search2(lat, lon, key))

    normalized_data = [normalize(entry) for entry in data]

    consolidated_df = pd.concat(normalized_data)

    date = datetime.now().strftime("%Y%m%d")

    consolidated_df.to_csv(f"data_analytics/openweather/Archivo_{date}.csv", index=False)
    
