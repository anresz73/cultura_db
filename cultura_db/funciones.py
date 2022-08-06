#

import requests
import csv
from datetime import datetime


def archivos_fuente():
    """
    Función trae los datos de archivos csv de la url y los crea localmente siguiendo la estructura definida
    """
    for categoria, url in csv_dicts.items():
        r = requests.get(url)
        #r_s = s.get(url_name)
        format_str = f'./{categoria}-%d-%m-%Y.csv'
        file_name = datetime.now().strftime(format_str).casefold()
        with open(file_name, 'w') as f:
            writer = csv.writer(f)
            for line in r.iter_lines():
                writer.writerow(line.decode('utf-8').split(','))
