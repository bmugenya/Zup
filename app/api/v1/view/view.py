from flask import Flask,render_template,Blueprint,Response
from flask_restful import Resource
from ..model.model import Model

api = Blueprint('api', __name__)

# HOME PAGE
class index(Resource,Model):
    def __init__(self):
        self.model = Model()

    def get(self):
        return Response(render_template('index.html'))


# CONTACT PAGE
class contact(Resource,Model):
    def __init__(self):
        self.model = Model()

    def get(self):
        return Response(render_template('contact.html'))


# ABOUT PAGE
class about(Resource,Model):
    def __init__(self):
        self.model = Model()

    def get(self):
        return Response(render_template('about.html'))



# DASHBOARD
class dashboard(Resource,Model):
    def __init__(self):
        self.model = Model()

    def get(self):
        return 'Dashboard'



# REGISTER
class addUsers(Resource,Model):
    def __init__(self):
        self.model = Model()

    def get(self):
        return Response(render_template('register.html'))


# LOGIN PAGE
class users(Resource,Model):
    def __init__(self):
        self.model = Model()

    def get(self):
        return Response(render_template('login.html'))

# CONFIGURATION
class config(Resource,Model):
    def __init__(self):
        self.model = Model()

    def get(self):
        return 'Configuraion Page'





# MAKE ANALYSIS
class analysis(Resource,Model):
    def __init__(self):
        self.model = Model()

    def get(self):
        return 'add analysis page'


#VIEW ANALYSIS
class details(Resource,Model):
    def __init__(self):
        self.model = Model()

    def get(self):
        return 'view analysis page'




# VIEW PAST ANALYSIS
class history(Resource,Model):
    def __init__(self):
        self.model = Model()

    def get(self):
        return 'Analysis history page'


# VIEW ALL REPORTED USERS
class report(Resource,Model):
    def __init__(self):
        self.model = Model()

    def get(self):
        return 'List of all available users'

