from datetime import datetime
import pandas as pd
from pandas import json_normalize
import json
from function import *

if __name__ == '__main__':
    with open('credenciales.txt', 'r') as f:
      key=f.read() 

    cityList = ["London", "New York", "Cordoba", "Taipei", "Buenos Aires", "Mexico DF", "Dublin", "Tilfis", "Bogota", "Tokio"] 

    for city in cityList:
       search(city,key)
       

