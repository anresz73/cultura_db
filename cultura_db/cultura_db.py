#

import locale
from .funciones.funciones_auxiliares import _sql_file_path
from .funciones.archivos_fuente import archivos_fuente
from .funciones.procesamiento_datos import procesamiento_datos
from .funciones.creacion_tablas import get_engine, write_tables, _drop_and_create_table, _write_table_from_df
from .constantes import *
from .settings import *

locale.setlocale(locale.LC_ALL, 'es_AR.UTF-8')

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
        Usa settings de variables de entorno
        """
        return get_engine(self.db_name, self.db_user, self.db_password, self.db_host, self.db_port)

    def crear_archivos_fuente(self):
        """
        Método para descargar las fuentes y descargarlas como csv con formato categoria-fecha.
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
        #write_tables(dict_tablas, _engine)

    def get_sql_file_path(self, table_name):
        """
        Contruye la ruta para acceder al archivo sql
        Args:
            table_name (str): nombre de la tabla
        """
        return _sql_file_path(table_name)
