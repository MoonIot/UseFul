from flask import Flask
from UseFul import AutoBlueprint

blueprints = AutoBlueprint(__package__, __file__)


def create_app() -> Flask:
    app = Flask(__name__)

    blueprints.init_app(app)
    
    
    blueprints.load_blueprints()

    return app
