#

import locale
import logging
import os
from .funciones import (
    get_engine,
    db_execute,
    _drop_and_create_table,
    _write_table_from_df,
    read_sql_file,
    procesamiento_datos,
    archivos_fuente,
    _sql_file_path
    )
from .constantes import *
from .settings import *
from .exceptions import *

# Idioma 
locale.setlocale(locale.LC_ALL, 'es_AR.UTF-8')

# Looging settings
dir = os.path.dirname(LOGGING_PATH)
if not os.path.isdir(dir):
    os.makedirs(dir)
log = logging.basicConfig(
    filename = LOGGING_PATH,
    level = logging.INFO,
    format = '%(asctime)s - %(levelname)s - %(module)s - %(message)s'
    )

# Clases
class Cultura_DB:
    """
    Clase que implementa la carga de archivos fuente, el procesamiento de los datos y la creación y actualizacion de las tablas en la base de datos
    """
    def __init__(self):
        # settings
        self.db_name = DB_NAME
        self.db_user = DB_USER
        self.db_password = DB_PASSWORD
        self.db_host = DB_HOST
        self.db_port = DB_PORT

        # Engine
        self.engine = self.get_engine_with_settings()

        # Constantes
        self.csv_urls = csv_urls

    def get_engine_with_settings(self):
        """
        Método  para conectarse a la base de datos Postgresql. Si la base de datos no existe la crea.
        Usa settings de las variables de entorno y función get_engine()
        """
        return get_engine(self.db_name, self.db_user, self.db_password, self.db_host, self.db_port)

    def crear_archivos_fuente(self):
        """
        Método para descargar las fuentes y descargarlas como csv con formato categoria-fecha.
        Trae los datos de archivos csv de la url y los crea localmente siguiendo la estructura definida en los csv
        Directorio base 
        """
        archivos_fuente(self.csv_urls)

    def procesar_datos(self):
        """
        Método de para procesar los datos provenientes de los arhivos csv.
        """
        return procesamiento_datos(self.csv_urls.keys())

    def crear_tablas(self, sql_file_path):
        """
        Método para crear tablas. Usa los scripts de archivos sql.
        Args:
            sql_file_path (str) : ruta de archivo sql
        """
        _drop_and_create_table(sql_file_path = sql_file_path, engine = self.engine)

    def actualizar_tablas(self, table_name, df_tabla):
        """
        Método para actualizar las tablas. Usa método .to_sql de pandas
        Args:
            table_name (str) : nombre de la tabla
            df_tabla (pd.dataframe) : dataframe con los datos para acutalizar
        """
        _write_table_from_df(table_name = table_name, df_tabla = df_tabla, engine = self.engine)

    def escribir_tablas(self):
        """
        Método unificado que usa crear_tablas y actualizar_tablas.
        """
        dict_datos = self.procesar_datos()
        for key, value in dict_datos.items():
            self.crear_tablas(sql_file_path = self.get_sql_file_path(key))
            self.actualizar_tablas(table_name = key, df_tabla = value)
        self.execute_sql('foreing_key')
        #write_tables(dict_tablas, _engine)

    def get_sql_file_path(self, file_name):
        """
        Contruye la ruta para acceder al archivo sql
        Args:
            file_name (str): nombre de la tabla
        """
        return _sql_file_path(file_name)
    
    def execute_sql(self, sql_file):
        """
        Método que ejecura un archivo con código sql
        Args:
            sql_file (str): nombre del archivo sql, en la carpeta sql
        """
        db_execute(
            read_sql_file(self.get_sql_file_path(sql_file)),
            self.engine
            )
