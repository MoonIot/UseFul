from flask import Flask
from UseFul import JwtApi

api = JwtApi(version='3.0.0~beta')


def create_app():
    app = Flask(__name__)

    app.config["secret_key"] = "adminadmin"

    api.init_app(app)

    from .resource import User, Posts
    api.add_api(User)

    return app
