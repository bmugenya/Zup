import os
from flask import (
    Flask,render_template,Blueprint,Response,redirect,
    url_for,request,current_app,make_response,jsonify
)
from flask_jwt_extended import (
    jwt_required, create_access_token,
    get_jwt_identity,set_access_cookies,unset_jwt_cookies,jwt_optional

)

from flask_restful import Resource
from ..model.model import Model
from ..model.tweepy_streamer import Twitter
from werkzeug.utils import secure_filename



api = Blueprint('api', __name__)


# CONTACT PAGE
class contact(Resource,Model):
    def __init__(self):
        self.model = Model()

    @jwt_optional
    def get(self):
        email = get_jwt_identity()
        return Response(render_template('contact.html',email=email))


# ABOUT PAGE
class about(Resource,Model):
    def __init__(self):
        self.model = Model()

    @jwt_optional
    def get(self):
        email = get_jwt_identity()
        return Response(render_template('about.html',email=email))

# HOMEPAGE
class index(Resource,Model):
    def __init__(self):
        self.user = Model()

    @jwt_optional
    def get(self):
        email = get_jwt_identity()
        return Response(render_template('index.html',email=email))

# MAKE ANALYSIS
class analysis(Resource,Twitter):
    def __init__(self):
        self.tweet = Twitter()

    @jwt_optional
    def get(self):
        email = get_jwt_identity()
        return Response(render_template('analysis.html',email=email))

    @jwt_optional
    def post(self):
        email = get_jwt_identity()
        user = request.form['topic']
        num_tweets = request.form['no']
        tweets=self.tweet.get_tweets(user,num_tweets)
        return Response(render_template("report.html",email=email,tweets=tweets))


#VIEW ALL ANALYSIS
class reports(Resource,Model):
    def __init__(self):
        self.model = Model()

    @jwt_optional
    def get(self):
        email = get_jwt_identity()
        return Response(render_template('reports.html',email=email))

# VIEW ONE ANALYSIS
class report(Resource,Model):
    def __init__(self):
        self.model = Model()

    @jwt_optional
    def get(self,report_id):
        email = get_jwt_identity()
        return Response(render_template('report.html',email=email))






