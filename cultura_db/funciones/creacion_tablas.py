#

import pandas as pd
from sqlalchemy import create_engine, text
from sqlalchemy_utils import database_exists, create_database

def get_engine(db_name, db_user, db_password, db_host, db_port):
    """
    Función para conectarse a la base de datos Postgresql con los parámetros pasados
    Si la base de datos no existe la crea.

    Args:
        db_name (str): Nombre de la base de datos
        db_user (str): Usuario
        db_password (str): Password
        db_host (str): Host
        db_port (int): Puerto que usa la bd
    """
    db_string = f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'
    if not database_exists(db_string):
        create_database(db_string)
    db_engine = create_engine(db_string)
    return db_engine

def db_execute(sql_stmt, sql_engine):
    """
    Función para ejecutar una sentencia SQL
    Args:
        sql_stmt (str): SQL query
        sql_engine (): engine inicializada con función get_engine()
    """
    t = text(text = sql_stmt)
    with sql_engine.connect() as connection:
        connection.execute(t) 