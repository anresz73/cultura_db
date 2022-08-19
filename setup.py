from setuptools import setup, find_packages

setup(
    name = 'cultura_db',
    version = '1.0.0',
    url = 'https://github.com/anresz73/cultura_db.git',
    description = 'Proyecto que trae datos desde archivos sql, procesa y construye base de datos Postgresql.',
    packages = find_packages(),
    #install_requires = []
)