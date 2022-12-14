# Script para traer las variables en .env

from decouple import config

DB_NAME = config('DB_NAME')
DB_USER = config('DB_USER')
DB_PASSWORD = config('DB_PASSWORD')
DB_HOST = config('DB_HOST')
DB_PORT = config('DB_PORT', cast = int)

DIRECTORIO_BASE = config('DIRECTORIO_BASE', cast = str)

LOGGING_PATH = config('LOGGING_PATH', cast = str)