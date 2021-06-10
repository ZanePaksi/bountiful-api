import json
from chalice import Blueprint
from chalicelib.test_data.users import USERS

user_routes = Blueprint(__name__)

@user_routes.route('/users')
def get_all_users():
    return json.dumps(USERS, indent=4)
