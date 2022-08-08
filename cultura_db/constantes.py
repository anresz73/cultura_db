#

csv_urls = {
    'museos' : r'https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/4207def0-2ff7-41d5-9095-d42ae8207a5d/download/museos_datosabiertos.csv',
    'cines' : r'https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/392ce1a8-ef11-4776-b280-6f1c7fae16ae/download/cine.csv',
    'bibliotecas' : r'https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/01c6c048-dbeb-44e0-8efa-6944f73715d7/download/biblioteca_popular.csv' 
    }

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
    'telefono' : 'str',
    'cod_area' : 'str',
    'mail' : 'str',
    'web' : 'str',
}