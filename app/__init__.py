from flask import Flask,render_template,Blueprint
from flask_restful import Resource

from .api.v1 import version_one as v1

def create_app():
    app = Flask(__name__)
    app.register_blueprint(v1)

    return app
