import json
from chalice import Blueprint, Response
from chalicelib.test_data.bounties import BOUNTIES

bounty_routes = Blueprint(__name__)

@bounty_routes.route('/bounties')
def get_all_bounties():
    return json.dumps(BOUNTIES, indent=4)

@bounty_routes.route('/bounties/{bounty_id}')
def get_bounty_by_id(bounty_id):
    result = __verify_bounty_id(bounty_id)
    return json.dumps(result, indent=4) if result else Response(status_code=404, body="Bounty not found")


def __verify_bounty_id(bounty_id):
    for bounty in BOUNTIES:
        if bounty_id == bounty['id']:
            return bounty
    return {}
