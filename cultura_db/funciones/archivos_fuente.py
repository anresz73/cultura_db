#

import requests
import csv
from datetime import datetime


def archivos_fuente(csv_dicts, format_str):
    """
    Función trae los datos de archivos csv de la url y los crea localmente siguiendo la estructura definida
    csv_dicts : dict - diccionario con las categorias y las urls de los datos 
    """
    for categoria, url in csv_dicts.items():
        #r = requests.get(url)
        #r_s = s.get(url_name)
        format_str = f'./{categoria}-%d-%m-%Y.csv'
        file_name = datetime.now().strftime(format_str).casefold()
        #with open(file_name, 'w') as f:
        #    writer = csv.writer(f)
        #    for line in r.iter_lines():
        #        writer.writerow(line.decode('utf-8').split(','))
        
        with requests.Session() as s:
            download = s.get(url)
            decoded_content = download.content.decode('utf-8')
            cr = csv.reader(decoded_content.splitlines(), delimiter = ',')
        return list(cr)
