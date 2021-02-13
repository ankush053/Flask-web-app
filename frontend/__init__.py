from flask import Flask , Blueprint
from frontend.routes.API.view import api
from frontend.routes.dashboard.view import dashboard
from frontend.routes.devices.view import devices
from frontend.config import config, databaseconfig
from frontend.routes.login.veiw import login
from flask_mongoengine import MongoEngine


def create_an_app():

    app = Flask(__name__)
    app.config.from_object(config)
    app.config["MONGODB_HOST"] = databaseconfig['URI']
    db = MongoEngine(app)

    app.register_blueprint(login)
    app.register_blueprint(api)
    app.register_blueprint(dashboard)
    app.register_blueprint(devices)

    return app

    
