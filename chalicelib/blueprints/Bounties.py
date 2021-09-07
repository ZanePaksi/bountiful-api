from chalicelib.loaders.bounty_client import BountyClient
from chalice import Blueprint, Response
import json, logging

class BountyService:

    def __init__(self, client):
        self.logger = logging.getLogger("Bounty Service")
        self.client = client

    def get_all_bounties(self, search_parameters={}):
        bounties = self.client.get_all_bounties(search_parameters)
        return [self.__build_bounty(bounty) for bounty in bounties]

    def get_bounty_by_id(self, id):
        bounty = self.client.get_bounty_by_id(id)
        return self.__build_bounty(bounty) if bounty else None

    def __build_bounty(self, bounty):
        return {
        'id': bounty[0],
        'creator_id': bounty[1],
        'hunter_id': bounty[2],
        'title': bounty[3],
        'description': bounty[4],
        'value': bounty[5]
        }

bounty_routes = Blueprint(__name__)
bounty_service = BountyService(BountyClient())

@bounty_routes.route('/bounties')
def get_bounties():
    search_parameters = bounty_routes.current_request.query_params
    bounties = bounty_service.get_all_bounties(search_parameters)
    return json.dumps(bounties, indent=4)

@bounty_routes.route('/bounties/{bounty_id}')
def get_by_id(bounty_id):
    bounty = bounty_service.get_bounty_by_id(bounty_id)
    return json.dumps(bounty, indent=4) if bounty else Response(status_code=404, body="Bounty not found")
