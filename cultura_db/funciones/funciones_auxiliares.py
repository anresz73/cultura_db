# Funciones auxiliares que se usan en más de uno de los compomentes y scripts.

from datetime import datetime

def _path_file(categoria):
    """
    Devuelve ruta archivo csv completo con fecha actual.
    In: 
    categoria : str - nombre de la categoría
    Out: 
    str - con ruta completa de archivo csv
    """
    estructura_ruta = f'./{categoria}/%Y-%B/{categoria}-%d-%m-%Y.csv'
    return datetime.now().strftime(estructura_ruta).casefold()

def _sql_file_path(tabla):
    """
    Devuelve el path completo 
    Args:
        tabla (str): nombre de la tabla
    """
    return f'./cultura_db/sql/{tabla}.sql'