#

import locale
from cultura_db.constantes import *

locale.setlocale(locale.LC_ALL, 'es_AR.UTF-8')

class Cultura_DB:
    """
    Clase
    """

    def __str__(self):
        return "cines"

    def __repr__(self):
        return "teatros"

    def get_archivos_fuente(self):
        """
        Método para ejecutar archivos_fuente
        """
        return archivos_fuente(csv_urls)

    def get_var(self):
        """
        Método de testeo
        """
        return csv_urls