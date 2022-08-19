# Funciones para creación de las tablas en la base de datos

import pandas as pd
import logging
from sqlalchemy import create_engine, text
from sqlalchemy_utils import database_exists, create_database
from os.path import basename, exists
from .procesamiento_datos import procesamiento_datos
from .funciones_auxiliares import _sql_file_path
from ..settings import *
from ..constantes import csv_urls
from ..exceptions import DBException

################################################################
# Funciones usadas en la clase Cultura_DB
################################################################

def get_engine(db_name, db_user, db_password, db_host, db_port):
    """
    Función para conectarse a la base de datos Postgresql con los parámetros pasados
    Si la base de datos no existe la crea.

    Args:
        In:
        db_name (str): Nombre de la base de datos
        db_user (str): Usuario
        db_password (str): Password
        db_host (str): Host
        db_port (int): Puerto que usa la bd
        Out: 
        engine creada
    """
    logging.info(f'Creando engine de db: {db_name}')
    db_string = f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'
    if not database_exists(db_string):
        try:
            create_database(db_string)
        except Exception as e:
            raise DBException(f'Error en la creación de la base de datos. Detalle: {e}.')
    db_engine = create_engine(db_string)
    return db_engine

def read_sql_file(sql_file_path):
    """
    Función que lee y devuelve archivo .sql
    Args:
        sql_file_path (str): path del archivo sql
        Out: str - sentencia sql
    """
    logging.info(f'Leyendo sql: {sql_file_path}')
    if not exists(sql_file_path):
        raise DBException(f'No existe archivo {sql_file_path}')
    with open(sql_file_path) as file:
        sql_query = file.read()
    return sql_query

# Funciones que crean tablas y las escriben
def db_execute(sql_stmt, sql_engine):
    """
    Función para ejecutar una sentencia SQL
    Args:
        sql_stmt (str): SQL query
        sql_engine (): engine inicializada con función get_engine()
    Ejecuta la sentencia
    """
    with sql_engine.connect() as connection:
        connection.execute(sql_stmt)

def _drop_and_create_table(sql_file_path, engine):
    """
    Función para crear la base de datos.
    Borra y crea la base de datos con las sentencias SQL en los archivos sql.
    Args:
        engine (sqlalchemy engine): conexión con la base de datos generada con get_engine o get_engine_with setting
        sql_file_path (str): ruta y nombre del archivo sql
    """
    logging.info(f'Creando nueva tabla: {sql_file_path}')
    db_execute(
        # Función read_sql_file creada antes
        sql_stmt = read_sql_file(sql_file_path),
        sql_engine = engine
        )

def _write_table_from_df(table_name, df_tabla, engine):
    """
    Función para escribir en la tabla desde DataFrame usando el método df.to_sql.
    No escribe el índice y agrega los datos a la tabla, usarlo después de drop_and_create_table con tabla vacía.
    Args:
        table_name (str): nombre de la tabla
        df_tabla (pd.DataFrame): df con los datos de la tabla. 
        engine (sqlalchemy engine): conexión con la base de datos generada con get_engine o get_engine_with setting
    """
    logging.info(f'Escribiendo tabla desde .to_sql: {table_name}')
    df_tabla.to_sql(table_name,
                    con = engine,
                    if_exists = 'append',
                    index = False
    )


################################################################
# Funciones de prueba no implementadas por la clase CulturaDB
################################################################

def drop_and_create_table():
    """
    Función que usa raw_conexion, cursor y sql queries directas.
    """
    _file_name = r'./cultura_db/sql/tabla_1.sql'
    _engine = get_engine(db_name = DB_NAME, db_user = DB_USER, db_password = DB_PASSWORD, db_host = DB_HOST, db_port = DB_PORT)
    connection, cursor = None, None
    connection = _engine.raw_connection()
    try:
        cursor = connection.cursor()
        #print('DROP TABLE IF EXISTS %s'.format(table_name))
        #cursor.execute("""DROP TABLE IF EXISTS %s""", table_name)
        cursor.execute(read_sql_file(sql_file_path = _file_name))
        connection.commit()
    except Exception as e:
        print(f'Error: {e}')
    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None:
            connection.close()

def write_table(table_name, df_tabla, engine):
    """
    Funcion que escribe las tablas en la base de datos.
    """
    #engine = get_engine(db_name = DB_NAME, db_user = DB_USER, db_password = DB_PASSWORD, db_host = DB_HOST, db_port = DB_PORT)
    #drop_and_create_table()
    logging.info(f'Creando y escribiendo tabla desde : {table_name}')
    _drop_and_create_table(
        engine = engine,
        sql_file_path = _sql_file_path(table_name) # r'./cultura_db/sql/tabla_1.sql'
    )
    #_tabla = procesamiento_datos(csv_urls.keys())[0]
    #_tabla_1 = _tabla_1.where(_tabla_1.notnull(), None)
    #table_name = basename(sql_file_path).split('.')[0]
    _write_table_from_df(
        table_name = table_name,
        df_tabla = df_tabla,
        engine = engine
    )

def _write_table():
    """
    Escribe las tablas en la base de datos
    """
    _engine = get_engine(db_name = DB_NAME, db_user = DB_USER, db_password = DB_PASSWORD, db_host = DB_HOST, db_port = DB_PORT)
    _file_name = r'./cultura_db/sql/tabla_1.sql'
    _stmt = read_sql_file(_file_name)
    db_execute(sql_stmt = _stmt, sql_engine = _engine)

def write_tables(dict_tablas, _engine):
    """
    Función que escribe las tres tablas. Implementado directamente en la clase CulturaDB
    Args:
        dict_tablas (dict) : Diccionario con las tablas provenientes de la función procesamiento de datos
    """
    #_engine = get_engine(db_name = DB_NAME, db_user = DB_USER, db_password = DB_PASSWORD, db_host = DB_HOST, db_port = DB_PORT)
    #_engine = get_engine_with_settings()
    for key, value in dict_tablas.items():
        write_table(
            table_name = key,
            df_tabla = value,
            engine = _engine
            )

def read_table():
    """
    Ejecuta sentencia sql 
    """
    return pd.read_sql(
        sql = 'SELECT * FROM tabla_1;',
        con = get_engine(db_name = DB_NAME, db_user = DB_USER, db_password = DB_PASSWORD, db_host = DB_HOST, db_port = DB_PORT),
        )

def get_engine_with_settings():
    """
    Función que devuelve el engine con las settings de las variables de settings.py
    """
    return get_engine(db_name = DB_NAME, db_user = DB_USER, db_password = DB_PASSWORD, db_host = DB_HOST, db_port = DB_PORT)
