# cultura_db
Proyecto de Base de Datos PostreSQL a partir de archivos fuente CSV.
# Deployment
Pasos para deployar.
Hay que tener instalados git, pip y docker en el sistema.
## Download
```sh
$ git clone https://github.com/anresz73/cultura_db.git
$ cd cultura_db/
```

## Entorno Virtual
```sh
$ python3 -m venv venv
$ source venv/bin/activate
```

## Dependencias
```sh
$ pip install -r requirements.txt
```

## Base de Datos
Opción con docker. Se puede descargar PostgreSQL desde https://www.postgresql.org/download/ también e instalarlo localmente.
```sh
$ docker run --name local-postgres -p 5432:5432 -e POSTGRES_PASSWORD=mysecretpassword -d postgres
```
#### Ejemplo
```python
import cultura_db
# Inicialización del objeto
db = cultura_db.Cultura_DB()
# Lectura y descarga de los archivos fuente
db.crear_archivos_fuente()
# Procesamiento y armado de los dataframes
db.procesar_datos()
# Conexión y escritura de base de datos y tablas
db.escribir_tablas()
```

#### Ejemplo 2
```python
print(db)
```
