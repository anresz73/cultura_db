#

import requests
import csv
import os
import logging
from datetime import datetime
from cultura_db.funciones import funciones_auxiliares
from ..exceptions import ArchivosFuenteException

#
def archivos_fuente(csv_dicts):
    """
    Función: trae los datos de archivos csv de la url y los crea localmente siguiendo la estructura definida
    In:
    csv_dicts : dict - diccionario con las categorias y las urls de los datos 
    Out: 
    Crea las carpetas y archivos respectivos
    """
    # Loop for que trae categorias y urls del diccionario
    logging.info('Inicio archivos_fuente()')
    for categoria, url in csv_dicts.items():
        # Armado de estructura de rutas y archivos csv con fecha actual
        path_file = funciones_auxiliares._path_file(categoria)
        path_base, file_name = os.path.split(path_file)
        # Datos del archivo csv usando requests
        try:
            logging.info(f'Leyendo url: {url}')
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
                raise ArchivosFuenteException(f'Error {r.status_code}')
        except Exception as e:
            raise ArchivosFuenteException(f'Error: {e}')