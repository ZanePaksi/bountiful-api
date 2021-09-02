import contextlib
from chalice import Chalice
import os, logging
import psycopg2

db_user = os.environ['DB_USER']
db_pass = os.environ['DB_PASS']
db_host = os.environ['DB_HOST']
db_port = os.environ['DB_PORT']
db_name = os.environ['DB_NAME']

dsn = f"dbname={db_name} user={db_user} password={db_pass} host={db_host} port={db_port}"
logger = logging.getLogger("DB ACCESS")

@contextlib.contextmanager
def db_connect():
    logger.debug(f'attemping to connect to db')
    try:
        connection = psycopg2.connect(dsn)
        yield connection
    finally:
        connection.close()

@contextlib.contextmanager
def db_cursor():
    logger.debug(f'attemping to create cursor')
    try:
        connection = psycopg2.connect(dsn)
        cursor = connection.cursor()
        yield cursor
    finally:
        cursor.close()
        connection.close()
