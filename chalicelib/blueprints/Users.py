from chalicelib.loaders.user_client import UserClient
from chalice import Blueprint, Response
import json, logging

class UserService:

    def __init__(self, client):
        self.logger = logging.getLogger("User Service")
        self.client = client

    def get_all_users(self):
        users = self.client.get_all_users()
        return [self.__build_user(user) for user in users]

    def get_user_by_id(self, id):
        user = self.client.get_user_by_id(id)
        return self.__build_user(user) if user else None

    def __build_user(self, user):
        return {
        'id': user[0],
        'username': user[1],
        'password': user[2],
        'email': user[3]
        }

user_routes = Blueprint(__name__)
user_service = UserService(UserClient())

@user_routes.route('/users', methods=['GET'])
def get_users():
    users = user_service.get_all_users()
    return json.dumps(users, indent=4)

@user_routes.route('/users', methods=['POST'])
def report_new_user():
    new_user_data = user_routes.current_request.json_body
    user_service.add_new_users(new_user_data)
    return json.dumps(new_user_data, indent=4)

@user_routes.route('/users/{user_id}', methods=['GET'])
def get_users(user_id):
    user = user_service.get_user_by_id(user_id)
    return json.dumps(user, indent=4) if user else Response(status_code=404, body="User not found")
