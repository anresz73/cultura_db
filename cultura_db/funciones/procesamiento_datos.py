# Armado de una función que procese todos los datos provenientes de los archivos csv.
# Normaliza las columnas, quita acentos, define los tipos de las columnas.
# Reemplaza nombres de columnas para unificarlas.
# Finalmente arma tres dataframes para poder ser exportados luegos a las tablas SQL.
# Falta Mmnejo de excepciones más detallado con columnas, filas y procesamientos.

import pandas as pd
import logging
from os.path import basename, split, exists
from .funciones_auxiliares import _path_file
from ..constantes import *
from ..exceptions import ProcesamientoDatosException

# Funciones específicas para usar en el procesamiento de datos
def _read_csv_custom(filepath):
    """
    Funcion customizada para la lectura de los archivos csv.
    Args:
        filepath (str): ruta y nombre de archivo csv
    Out: pd.DataFrame leído
    """
    if not exists(filepath):
        raise ProcesamientoDatosException(f'No existe la ruta {filepath}')
    df_csv = pd.read_csv(
        # uso funcion auxiliar de armado de ruta y nombre archivo
        filepath,
        # Tipos específicos
        dtype = DTYPES_DICT_READ,
        # valores NaN
        na_values = NA_VALUES,
        # Funciones para aplicar en determinadas columnas
        converters = CONVERTERS,
        )
    # Sanity check
    if df_csv.columns.size < 2:
        raise ProcesamientoDatosException(f'Error de fuente {filepath}.')
    return df_csv

def _custom_merge(df_datos, columna, list_columnas):
    """
    Funcion que devuelve df de dos columnas unidas manteniendo los valores originales nan.
    Args:
        df_datos (DataFrame): df con los dos campos de datos a ser unidos
        columna (str): nombre de la columna para crear
        list_columnas (list): nombres de las dos columnas
    Out: pd.DataFrame
    """
    if not all([e in df_datos.columns for e in list_columnas]):
        raise ProcesamientoDatosException(f'Nombre de columnas no incluídos en df.')
    df_datos = df_datos.loc[:, list_columnas].copy()
    mask = df_datos.notna().all(axis = 1)
    df_datos[columna].loc[mask] = df_datos.loc[mask].apply(' '.join, axis = 1)
    return df_datos[columna]

#Función general customizada para todos los csv
def procesamiento_datos(list_categorias):
    """
    Función que normaliza la información de los archivos csv de categorías 
    museos, salas de cine, bibliotecas.
    Args:
        In:
        list_categorias : list - iter : lista o iterable con las categorias
        Out:
        Dict con keys = [tabla_123], values = 3 DataFrame
    """
    # Loop for general para leer cada csv y aplicar filtrado y reordenamiento en los DataFrames 
    # Lista para agregar los tres dfs.
    df_list = []
    for categoria in list_categorias:
        logging.info(f'Leyendo csv categoría: {categoria}')
        # Lectura del csv
        filepath = _path_file(categoria)
        df = _read_csv_custom(filepath)
        # Limpieza y normalización de columnas
        df.columns = df.columns.str.casefold()
        df.columns = df.columns.map(lambda x: x.translate(TRANSLATE))
        df = df.rename(columns = COLUMNAS_RENAMER)
        # Normalizar columnas específicas - Provincias con y sin acentos
        df[CATEGORIA_PROVINCIA] = df[CATEGORIA_PROVINCIA].map(lambda x: x.translate(TRANSLATE)).str.casefold()
        # Asignación de tipos específicos - Uso de método convert_dtypes en vez de customizar todas los tipos por columna
        df = df.convert_dtypes()
        # Loop for para unir las columnas indicadas (teléfono, dirección o domicilio)
        for key, value in COLUMNA_MERGE.items():
            df[key] = _custom_merge(df, key, value)
        # Agrega columna con la fuente (nombre del archivo csv)
        df[CATEGORIA_FUENTE] = basename(filepath)
        # Se agrega el dataframe a la lista
        df_list.append(df)

    # Tabla 1
    logging.info(f'Procesando Tabla 1')
    # Uso de concat para armar la tabla unificada con las columnas seleccionadas
    result_1 = pd.concat(
        objs = df_list,
        axis = 0
        ).loc[:, COLUMNAS + [CATEGORIA_FUENTE]]

    # Diccionarios 
    # Con id_provincia como clave y provincia como valores
    dict_result = {k : v for k, v in zip(list_categorias, df_list)}
    # Con id_provincia como clave y provincia como valores
    dict_provincias = result_1.loc[:, [COLUMNA_AGRUPAR, CATEGORIA_PROVINCIA]].drop_duplicates().set_index(COLUMNA_AGRUPAR).to_dict()[CATEGORIA_PROVINCIA]

    # Tabla 2
    logging.info('Procesando Tabla 2')
    result_2 = []
    for categoria_registro in [CATEGORIA_FUENTE, CATEGORIA_CATEGORIAS]:
        result_2.append(result_1.groupby(categoria_registro).size())
    # Chequear la tabla que se busca obtener!!!!!!!
    df_aux = result_1.groupby([CATEGORIA_PROVINCIA, CATEGORIA_CATEGORIAS], as_index = True).size()
    idx = [f'{e[0]}-{e[1]}' for e in df_aux.index]
    df_aux.index = idx
    result_2.append(df_aux)
    result_2 = pd.concat(result_2, axis = 0).reset_index()
    result_2.columns = [ITEMS, CANTIDAD_REGISTROS]

    # Tabla 3
    logging.info('Procesando Tabla 3')
    # Uso de groupby con el diccionario en la categoría cine y la función agregada definida con valores a contar y sumar
    result_3 = dict_result[CATEGORIA_CINES].groupby(COLUMNA_AGRUPAR, as_index = False).agg(
        AGGREGATOR_DICT)
    result_3.loc[:, CATEGORIA_PROVINCIA] = result_3[COLUMNA_AGRUPAR].astype(int).copy().replace(dict_provincias)

    # Armado del diccionario para el retorno de la función
    keys = [f'tabla_{e + 1}' for e in range(3)]
    result = {k : v for k, v in zip(keys, [result_1, result_2, result_3])}

    #return result_1, result_2, result_3
    return result
