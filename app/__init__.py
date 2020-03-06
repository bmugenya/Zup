import os
from flask import Flask,Blueprint
from flask_restful import Resource

from .api.v1 import version_one as v1
from .db_con import database_setup

UPLOAD_FOLDER ='app/static/img'


def create_app():
    app = Flask(__name__)
    app.register_blueprint(v1)

    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

    return app
