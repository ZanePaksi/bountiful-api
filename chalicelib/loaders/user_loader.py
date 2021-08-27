from chalice import Chalice
from chalicelib.blueprints.Acesss import db_connect
import psycopg2

def add_new_users(users):
    connection = db_connect()
    while connection.cursor() as c:
        for user in users:
            c.execute("INSERT INTO users (username, password) VALUES (%s, %s)", user['Username'], user['password'])
        c.commit()
