from .model.model import Model
from .view.view import *
from .view.user import *


from flask_restful import Api, Resource
from flask import Blueprint


version_one = Blueprint('api_v1', __name__, url_prefix='/api/v1')
api = Api(version_one)


api.add_resource(index, "/")
api.add_resource(contact, "/contact")
api.add_resource(about, "/about")
api.add_resource(addUsers, "/adduser")
api.add_resource(users, "/user")
api.add_resource(config, "/config")
api.add_resource(analysis, "/analysis")
api.add_resource(reports, "/reports")
api.add_resource(report, "/report/<int:report_id>")
api.add_resource(logout, "/logout")


