from setuptools import setup, find_packages

setup(
    name = 'cultura_db',
    version = '1.0.0',
    url = 'https://github.com/anresz73/cultura_db',
    download_url = 'https://github.com/anresz73/cultura_db',
    description = 'Proyecto que trae datos desde archivos sql, procesa y construye base de datos Postgresql.',
    packages = [
        'cultura_db', 
        'cultura_db/funciones',
        'cultura_db/sql',
    ],
    #install_requires = []
)