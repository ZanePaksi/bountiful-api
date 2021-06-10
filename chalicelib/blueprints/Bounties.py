import json
from chalice import Blueprint
from chalicelib.test_data.bounties import BOUNTIES

bounty_routes = Blueprint(__name__)

@bounty_routes.route('/bounties')
def get_all_bounties():
    return json.dumps(BOUNTIES, indent=4)
