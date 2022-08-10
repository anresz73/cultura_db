# Armado de una función que procese todos los datos provenientes de los archivos csv.
# Normaliza las columnas, quita acentos, define los tipos de las columnas.
# Reemplaza nombres de columnas para unificarlas.
# Finalmente arma tres dataframes para poder ser exportados luegos a las tablas SQL.

import pandas as pd
from ..constantes import *
from .funciones_auxiliares import _path_file

def procesamiento_datos(list_categorias):
    """
    Función que normaliza la información de los archivos csv de categorías 
    museos, salas de cine, bibliotecas.
    In:
    list_categorias : list - iter : lista o iterable con las categorias
    Out:
    Tupla con los tres DataFrame
    """
    df_list = []
    for categoria in list_categorias:
        df = pd.read_csv(
            _path_file(categoria),
            na_values = ['s/d'],
            converters = {'espacio_INCAA' : lambda x: True if x.casefold() == 'si' else False},
            )
        df.columns = df.columns.str.casefold()
        df = df.rename(columns = COLUMNAS_RENAMER)
        df = df.astype(DTYPES_DICT)
        df['domicilio'] = df[['domicilio', 'piso']].apply(' '.join, axis = 1)
        df['telefono'] = df[['cod_area', 'telefono']].apply(' '.join, axis = 1)
        df_list.append(df)

    dict_result = {k : v for k, v in zip(list_categorias, df_list)}

    result_1 = pd.concat(
        objs = df_list,
        axis = 0
        ).loc[:, COLUMNAS]
    
    result_2 = None

    result_3 = dict_result[CATEGORIA_CINES].groupby(dict_result[CATEGORIA_CINES][COLUMNA_AGRUPAR]).agg(
        AGGREGATOR_DICT)

    return result_1, result_2, result_3
