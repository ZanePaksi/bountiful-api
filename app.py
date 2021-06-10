from chalice import Chalice
from chalicelib.blueprints.Users import user_routes
from chalicelib.blueprints.Login import login_routes
from chalicelib.blueprints.Bounties import bounty_routes

app = Chalice(app_name='bountiful-api')

app.register_blueprint(user_routes)
app.register_blueprint(login_routes)
app.register_blueprint(bounty_routes)
