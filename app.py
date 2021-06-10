from chalice import Chalice
from chalicelib.blueprints.Bounties import bounty_routes
from chalicelib.blueprints.Users import user_routes

app = Chalice(app_name='bountiful-api')

app.register_blueprint(bounty_routes)
app.register_blueprint(user_routes)

@app.route('/')
def index():
    return {'hello': 'world'}
