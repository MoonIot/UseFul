from flask import Blueprint

bp = Blueprint('panel', __name__)

from .routes import *