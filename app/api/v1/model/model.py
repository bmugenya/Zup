from ....db_con import database_setup
from passlib.apps import custom_app_context as pwd_context
from datetime import datetime, date, time, timedelta
import tweepy


class Model():

    def __init__(self):
        self.database = database_setup()
        self.cursor = self.database.cursor

    def save_users(self, fname,lname, email,password, photo):

        user = {
            "fname": fname,
            "lname": lname,
            "email": email,
            "password":pwd_context.encrypt(password),
            "photo": photo
        }

        query = """INSERT INTO Users (fname,lname,email,password,photo)
            VALUES(%(fname)s,%(lname)s,%(email)s, %(password)s,%(photo)s);"""
        self.cursor.execute(query, user)
        self.database.conn.commit()

        return user

    def add_config(self,email):

        config = {
            "consumerKey": "r7fHaRwhccxQXFuN9nmQCHYiI",
            "consumerSecret": "T2A5Sxs1rHyx5P1HgFDnQ5VQd7tXPv0DEsFEYjLCojEsgJlThx",
            "accessToken":  "1005899876742377474-WuxZRYNt3dwEM62D4gCrnZEW6vtnKo",
            "accessSecret":"IBxDDAVK7ptPumqxeslnUR6TfLpVT1CpXBgQzEfXGNgnA",
            "email": email
        }

        query = """INSERT INTO Config (consumerKey,consumerSecret,accessToken,accessSecret,email)
            VALUES(%(consumerKey)s,%(consumerSecret)s,%(accessToken)s, %(accessSecret)s,%(email)s);"""
        self.cursor.execute(query, config)
        self.database.conn.commit()

        return config





    def login(self, email, password):

        query = "SELECT password FROM Users WHERE email = '%s';" % (email)
        self.cursor.execute(query)
        pwd = self.cursor.fetchone()

        if pwd:
            if pwd_context.verify(password, pwd[0]):
                query = "SELECT fname,lname,email,photo FROM Users WHERE email = '%s';" % (email)
                self.cursor.execute(query)
                users = self.cursor.fetchone()

                return users

    def check_email(self,r_email):
        query = "SELECT email FROM Users WHERE email = '%s';" % (r_email)
        self.cursor.execute(query)
        users = self.cursor.fetchone()

        return users

    def get_user(self,email):
        query = "SELECT fname,lname,photo,user_id FROM Users WHERE email = '%s';" % (email)
        self.cursor.execute(query)
        users = self.cursor.fetchone()

        return users






