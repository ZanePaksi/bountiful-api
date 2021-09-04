import json
from chalice import Blueprint, Response
from chalicelib.loaders.bounty_loader import get_all_bounties, get_bounty_by_id

bounty_routes = Blueprint(__name__)

@bounty_routes.route('/bounties')
def get_bounties():
    bounties = get_all_bounties()
    return json.dumps(bounties, indent=4)

@bounty_routes.route('/bounties/{bounty_id}')
def get_by_id(bounty_id):
    result = get_bounty_by_id(bounty_id)
    return json.dumps(result, indent=4) if result else Response(status_code=404, body="Bounty not found")
