import os
from flask import Flask,render_template,Blueprint,Response,redirect,url_for,request,current_app
from flask_restful import Resource
from ..model.model import Model
from werkzeug.utils import secure_filename

api = Blueprint('api', __name__)

# REGISTER
class addUsers(Resource,Model):
    def __init__(self):
        self.user = Model()

    def allowed_file(filename):
        return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

    def get(self):
        return Response(render_template('register.html'))


    def post(self):
        file = request.files['file']
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
            photo=filename


        fname = request.form['fname']
        lname = request.form['lname']
        email=request.form['email']
        password=request.form['pword']

        is_present = self.user.check_email(email)

        if is_present:
            return redirect(url_for('api_v1.addusers'))

        self.user.save_users(fname,lname,email,password,photo)

        return redirect(url_for('api_v1.index'))




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



# HOMEPAGE
class index(Resource,Model):
    def __init__(self):
        self.model = Model()

    def get(self):
        return Response(render_template('index.html'))


# LOGIN PAGE
class users(Resource,Model):
    def __init__(self):
        self.user = Model()

    def get(self):
        return Response(render_template('login.html'))

    def post(self):
        email = request.form['email']
        password = request.form['pword']

        user = self.user.login(email,password)


        if user:
           return redirect(url_for('api_v1.index'))
        return redirect(url_for('api_v1.addusers'))

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

