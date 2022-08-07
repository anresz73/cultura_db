#

import requests
import csv
import os
from datetime import datetime


def archivos_fuente(csv_dicts):
    """
    Función: trae los datos de archivos csv de la url y los crea localmente siguiendo la estructura definida
    In:
    csv_dicts : dict - diccionario con las categorias y las urls de los datos 
    Out: 
    
    """
    for categoria, url in csv_dicts.items():
        #r = requests.get(url)
        #r_s = s.get(url_name)
        estructura_ruta = f'./{categoria}/%Y-%B/{categoria}-%d-%m-%Y.csv' #
        path_file = datetime.now().strftime(estructura_ruta).casefold()
        head, tail = os.path.split(path_file)
        #with open(file_name, 'w') as f:
        #    writer = csv.writer(f)
        #    for line in r.iter_lines():
        #        writer.writerow(line.decode('utf-8').split(','))
        print(f'Ruta: {path_file}\nHead: {head}\nTail: {tail}\n')
        #with requests.Session() as s:
        #    download = s.get(url)
        #    decoded_content = download.content.decode('utf-8')
        #    cr = csv.reader(decoded_content.splitlines(), delimiter = ',')
        #return list(cr)
