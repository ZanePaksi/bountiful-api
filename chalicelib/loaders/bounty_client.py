from chalice import Chalice
import os, logging, psycopg2
from .access import db_cursor
from .search_builder import BountySearchBuilder

class BountyClient:

    def __init__(self):
        self.logger = logging.getLogger("Bounty Client")
        self.search_builder = BountySearchBuilder('bounties')

    def get_all_bounties(self, search_parameters={}):
        bounties = []
        with db_cursor(os.environ) as c:
            c.execute(self.search_builder.build_search_query(search_parameters))
            bounties = c.fetchall()
        return bounties

    def get_bounty_by_id(self, id):
        bounty = []
        with db_cursor(os.environ) as c:
            c.execute(f"SELECT * FROM bounties WHERE bounty_id = {id};")
            bounty = c.fetchone()
        return bounty if bounty else None

    def add_new_bounty(self, bounty):
        with db_connect(os.environ) as conn:
            c = conn.cursor()
            self.create_bounty_table(c)
            if bounty:
                c.execute("""
                    INSERT INTO bounties (creator_id, hunter_id, title, description, value)
                        VALUES (%s, %s, %s, %s, %s)""",
                        (bounty['creator_id'], bounty['hunter_id'], bounty['title'],
                        bounty['desc'], bounty['value'])
                )
            else:
                raise ValueError("Bounty is of NoneType")

    def create_bounty_table(self, cursor):
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS bounties (
            		bounty_id serial PRIMARY KEY,
            		creator_id INT,
            		hunter_id INT,
            		title VARCHAR ( 50 ) NOT NULL,
               	    description text NOT NULL,
            		value INT CHECK (value > 0),
            		CONSTRAINT creator_id FOREIGN KEY(creator_id) REFERENCES users(user_id) ON DELETE SET NULL,
             		CONSTRAINT hunter_id FOREIGN KEY(hunter_id) REFERENCES users(user_id) ON DELETE SET NULL
            );"""
        )
