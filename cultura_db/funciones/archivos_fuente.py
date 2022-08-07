#

#from genericpath import isdir
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
    Crea las carpetas y archivos respectivos
    """
    # Loop for que trae categorias y urls del diccionario
    for categoria, url in csv_dicts.items():
        # Armado de estructura de rutas y archivos csv con fecha actual
        estructura_ruta = f'./{categoria}/%Y-%B/{categoria}-%d-%m-%Y.csv' #
        path_file = datetime.now().strftime(estructura_ruta).casefold()
        path_base, file_name = os.path.split(path_file)
        # Datos del archivo csv usando requests
        try:
            r = requests.get(url)
            if r.status_code == 200:
                #csv_rows = r.content.decode('utf-8').splitlines()
                #csv_rows = [[e] for e in r.iter_lines()]
                csv_rows = csv.reader(r.content.decode('utf-8').splitlines(), delimiter = ',')
                # Creación de carpeta
                if not os.path.isdir(path_base):
                    os.makedirs(path_base)
                # Creación de archivo csv. Lo reemplaza si ya existe por opción 'w'
                with open(path_file, 'w') as f:
                    writer = csv.writer(f, delimiter = ',')
                    writer.writerows(csv_rows)
                #print(f'Ruta: {path_file}\nHead: {file_name}\nTail: {path_base}\n')
            else:
                raise Exception(f'Error {r.status_code}')
        except:
            raise Exception('Error')
            #OJO customizar después las excepcciones