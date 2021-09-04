import contextlib
from chalice import Chalice
import os, logging
import psycopg2

logger = logging.getLogger("DB ACCESS")

@contextlib.contextmanager
def db_connect(config):
    logger.debug(f'attemping to connect to db')
    try:
        dsn = build_dsn(config)
        connection = psycopg2.connect(dsn)
        yield connection
    finally:
        connection.close()

@contextlib.contextmanager
def db_cursor(config):
    logger.debug(f'attemping to create cursor')
    try:
        dsn = build_dsn(config)
        connection = psycopg2.connect(dsn)
        cursor = connection.cursor()
        yield cursor
    finally:
        cursor.close()
        connection.close()

def build_dsn(config):
    db_user = config['DB_USER']
    db_pass = config['DB_PASS']
    db_host = config['DB_HOST']
    db_port = config['DB_PORT']
    db_name = config['DB_NAME']
    return f"dbname={db_name} user={db_user} password={db_pass} host={db_host} port={db_port}"
