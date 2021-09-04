from chalice import Chalice
import psycopg2, os
from .access import db_connect, db_cursor

def get_all_bounties():
    bounties = []
    with db_cursor(os.environ) as c:
        c.execute("SELECT * FROM bounties;")
        bounties = c.fetchall()
    return [assemble_bounty_object(bounty) for bounty in bounties]

def get_bounty_by_id(id):
    bounty = []
    with db_cursor(os.environ) as c:
        c.execute(f"SELECT * FROM bounties WHERE bounty_id = {id};")
        bounty = c.fetchone()
    return assemble_bounty_object(bounty) if bounty else None

def assemble_bounty_object(bounty):
    return {
    'id': bounty[0],
    'creator_id': bounty[1],
    'hunter_id': bounty[2],
    'title': bounty[3],
    'description': bounty[4],
    'value': bounty[5]
    }
