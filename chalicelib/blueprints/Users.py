import json
from chalice import Blueprint
from chalicelib.test_data.users import USERS
from chalicelib.loaders.user_loader import add_new_users

user_routes = Blueprint(__name__)

@user_routes.route('/users', methods=['GET'])
def get_all_users():
    return json.dumps(USERS, indent=4)

# CURRENTLY RIGHT HERE: WORKING ON SENDING USER IN, AND WRITING IT, THEN NEED TO WRITE RETRIEVALS
@user_routes.route('/users', methods=['POST'])
def report_new_user():
    new_user_data = user_routes.current_request.json_body
    return json.dumps(new_user_data, indent=4)
