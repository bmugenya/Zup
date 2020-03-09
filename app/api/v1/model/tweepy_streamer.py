from ....db_con import database_setup
from passlib.apps import custom_app_context as pwd_context
from datetime import datetime, date, time, timedelta


from tweepy import API
from tweepy import OAuthHandler



class Twitter():

    def __init__(self):
        self.database = database_setup()
        self.cursor = self.database.cursor

        self.auth = self.authenticate_twitter_app()
        self.twitter_client = API(self.auth)
        self.twitter_user = None

    def authenticate_twitter_app(self):
        auth = OAuthHandler('a4eoZrfLDcN7Iyyv9fpSaDO8w', 'oxhkG0o8Y6epVKRPavt2gXTxk3pnzOSFgg38sjdQ6DRAC2B7gy')
        auth.set_access_token('1005899876742377474-2VFZ3XR2PNZDwXVX6IHcGnSbcrFhah', 'DbLRrvdifUrKMELrjR5HlwTbtUMBw4IgYPV1MtP5505jm')
        return auth



    def get_twitter_client_api(self):
        return self.twitter_client

    def get_tweets(self,user,num_tweets):
        tweets = self.twitter_client.user_timeline(screen_name=user, count=num_tweets)
        return [{'tweet': t.text,
        'created_at': t.created_at,
        'username': user,
        'headshot_url': t.user.profile_image_url} for t in tweets]





