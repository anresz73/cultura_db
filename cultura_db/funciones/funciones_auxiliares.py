# Funciones auxiliares que se usan en más de uno de los compomentes y scripts.

from datetime import datetime
from ..constantes import DIRECTORIO_BASE

def _path_file(categoria):
    """
    Devuelve ruta archivo csv completo con fecha actual.
    In: 
    categoria : str - nombre de la categoría
    Out: 
    str - con ruta completa de archivo csv
    """
    estructura_ruta = f'./{DIRECTORIO_BASE}/{categoria}/%Y-%B/{categoria}-%d-%m-%Y.csv'
    return datetime.now().strftime(estructura_ruta).casefold()

def _sql_file_path(table_name):
    """
    Devuelve el path completo 
    Args:
        table_name (str): nombre de la tabla
    """
    return f'./cultura_db/sql/{table_name}.sql'