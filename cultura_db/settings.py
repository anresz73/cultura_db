#

from decouple import config

DB_NAME = config('DB_NAME')
DB_USER = config('DB_USER')
DB_PASSWORD = config('DB_PASSWORD')
DB_HOT = config('DB_HOT')
DB_PORT = config('DB_PORT', cast = int)