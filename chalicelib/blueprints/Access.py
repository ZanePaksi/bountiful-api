from chalice import Chalice
import psycopg2

db_user = os.environ['DB_USER']
db_pass = os.environ['DB_PASS']
db_host = os.environ['DB_HOST']
db_port = os.environ['DB_PORT']

def db_connect():
    with psycopg2.connect(user=db_user, password=db_pass, db_host, db_port) as connection:
        yield connection
