# cultura_db
Proyecto de Base de Datos PostreSQL a partir de archivos fuente CSV.
# Deployment
Pasos para deployar.
## Download
* git clone https://github.com/anresz73/cultura_db.git
* cd cultura_db/

## Entorno Virtual
* python3 -m venv venv
* source venv/bin/activate

## Dependencias
* pip install --requirement requirements.txt

## Base de Datos
* docker run --name local-postgres -p 5432:5432 -e POSTGRES_PASSWORD=mysecretpassword -d postgres

