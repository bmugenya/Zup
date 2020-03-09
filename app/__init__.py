import os
from flask import Flask,Blueprint
from flask_restful import Resource

from .api.v1 import version_one as v1
from .db_con import database_setup
from flask_jwt_extended import JWTManager



UPLOAD_FOLDER ='app/static/img'


def create_app():
    app = Flask(__name__)
    app.register_blueprint(v1)

    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    app.secret_key ="371a7a78d634dd71ce5f215d4827ea919d00ea50a9e20482d7adefd8a5156b78"

    JWTManager(app)
    jwt = JWTManager(app)
    app.config['JWT_TOKEN_LOCATION'] = ['cookies']
    app.config['JWT_ACCESS_COOKIE_PATH'] = '/'
    app.config['JWT_COOKIE_CSRF_PROTECT'] = False





    return app
