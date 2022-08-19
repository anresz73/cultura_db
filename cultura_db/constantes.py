# Variables y constantes aplicadas en las distintas funciones y métodos

# Diccionario con las categorías y urls de los archivos csv a descargar y procesar.
csv_urls = {
    'museos' : r'https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/4207def0-2ff7-41d5-9095-d42ae8207a5d/download/museos_datosabiertos.csv',
    'cines' : r'https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/392ce1a8-ef11-4776-b280-6f1c7fae16ae/download/cine.csv',
    'bibliotecas' : r'https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/01c6c048-dbeb-44e0-8efa-6944f73715d7/download/biblioteca_popular.csv' 
    }

# Lectura csv general
# Constantes configuradas para el procesamiento y limpiezo de los DFs.
# List - Nombre de las columnas ordenadas para pasar al df 
COLUMNAS = [
    'cod_localidad',
    'id_provincia',
    'id_departamento',
    'categoria',
    'provincia',
    'localidad',
    'nombre',
    'domicilio', # 'piso',
    'codigo_postal',
    'telefono', # 'cod_area',
    'mail',
    'web',
    ]

# Diccionario para renombrar las columnas que difieren en los tres csvs
COLUMNAS_RENAMER = {
    'cod_loc' : 'cod_localidad',
    'idprovincia' : 'id_provincia',
    'iddepartamento' : 'id_departamento',
    'categoría' : 'categoria',
    'dirección' : 'domicilio',
    'direccion' : 'domicilio',
    'teléfono' : 'telefono',
    'cp' : 'codigo_postal',
    'cod_tel' : 'cod_area'
    }

# Diccionario con los tipos para la lectura inicial de los archivos csv
merge_type = 'str'
merge_columnas = ['cod_area', 'Cod_tel', 'Teléfono', 'telefono', 'Dirección', 'Domicilio', 'direccion', 'Piso', 'piso']
DTYPES_DICT_READ = {col : merge_type for col in merge_columnas}

# Diccionario con los tipos de cada columna usada
DTYPES_DICT = {
    'cod_localidad' : 'str',
    'id_provincia' : 'int',
    'id_departamento' : 'int',
    'categoria' : 'str',
    'provincia' : 'str',
    'localidad' : 'str',
    'nombre' : 'str',
    'domicilio' : 'str',
    'piso' : 'str',
    'codigo_postal' : 'str',
    #'telefono' : 'str',
    'cod_area' : 'str',
    'mail' : 'str',
    'web' : 'str',
}

# Valores para confirgurar el filtrado y limpieza de la información provenientes de los archivos csv
# Valores a considerar como NaN.
NA_VALUES = ['s/d']
# Dict para customizar con función lambda anónima la columna de espacio_INCAA
CONVERTERS = {'espacio_INCAA' : lambda x: True if x.casefold() == 'si' else False}
# Columnas a unir, teléfonos y direcciones o domicilios. Manteniendo el orden dado en los values.
COLUMNA_MERGE = {
    'domicilio' : ['domicilio', 'piso'],
    'telefono' : ['cod_area', 'telefono']
}
# Filtrado de acentos
TRANSLATE = str.maketrans('áéíóú', 'aeiou')

# Nombre columna fuentes
CATEGORIA_FUENTE = 'fuente'

# Tabla Nro 3.
# Categoría en type str de los cines
CATEGORIA_CINES = 'cines'
CATEGORIA_PROVINCIA = 'provincia'
CATEGORIA_CATEGORIAS = 'categoria'
# Columna para ser procesada y contar y sumar pantallas, butacas y espacio_incaa
COLUMNA_AGRUPAR = 'id_provincia'
# Diccionario que indica que función se aplica en cada caso, sum o count
AGGREGATOR_DICT = {'pantallas' : 'sum', 'butacas' : 'sum', 'espacio_incaa' : 'sum'}
#
ITEMS = 'items'
CANTIDAD_REGISTROS = 'cantidad_registros'

