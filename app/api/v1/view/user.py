import os
from flask import (
    Flask,render_template,Blueprint,Response,redirect,
    url_for,request,current_app,make_response
)
from flask_jwt_extended import (
    jwt_required, create_access_token,
    get_jwt_identity,set_access_cookies,unset_jwt_cookies,jwt_optional

)

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
            access_token = create_access_token(identity=email, expires_delta=False)
            # Set the JWT cookies in the response
            resp = make_response(redirect(url_for('api_v1.index')))
            set_access_cookies(resp, access_token)
            return resp

        return redirect(url_for('api_v1.users'))

# LOGOUT PAGE
class logout(Resource, Model):
    def __init__(self):
        self.user = Model()

    @jwt_required
    def post(self):
        resp = make_response(redirect(url_for('api_v1.index')))
        unset_jwt_cookies(resp)
        return resp



# CONFIGURATION
class config(Resource,Model):
    def __init__(self):
        self.model = Model()

    @jwt_optional
    def get(self):
        email = get_jwt_identity()
        return Response(render_template('config.html',email=email))


