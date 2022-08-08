#

import pandas as pd
from cultura_db.constantes import *

from cultura_db.funciones import funciones_auxiliares

def procesamiento_datos(list_categorias):
    """
    Función que normaliza la información de los archivos csv de categorías 
    museos, salas de cine, bibliotecas.
    In:
    list_categorias : list - iter : lista o iterable con las categorias
    """
    df_list = []
    for categoria in list_categorias:
        data = pd.read_csv(funciones_auxiliares._path_file(categoria))
        data.columns = data.columns.str.casefold()
        data = data.rename(columns = COLUMNAS_RENAMER)
        df_list.append(data)

    result = pd.concat(
        objs = df_list,
        axis = 0
        )

    return result.loc[:, COLUMNAS]
