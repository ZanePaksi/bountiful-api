import json
from chalice import Blueprint, Response
from chalicelib.test_data.users import USERS

login_routes = Blueprint(__name__)

@login_routes.route('/login', methods=['GET'])
def attempt_login():
    if len(login_routes.current_request.query_params) > 1:
        credentials = __gather_login_credentials(login_routes.current_request.query_params)
        valid_user = __validate_credentials(credentials)
        return json.dumps(valid_user, indent=4) if valid_user else Response(status_code=404, body="Invalid Username or Password")
    else:
        return Response(status_code=403, body="username and password required")

def __gather_login_credentials(request_parameters):
    credential_parameters = ['username', 'password']
    credentials = {}
    for parameter in request_parameters:
        if parameter in credential_parameters:
            credentials[parameter] = request_parameters[parameter]
    if len(credentials) > 1:
        return credentials
    else:
        raise(ValueError)

def __validate_credentials(credentials):
    for user in USERS:
        if credentials['username'] == user['username']:
            print("username found")
            if credentials['password'] == user['password']:
                print('password matched')
                return user
    return {}
