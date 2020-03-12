from ....db_con import database_setup
from passlib.apps import custom_app_context as pwd_context
from datetime import datetime, date, time, timedelta
from flask import jsonify


from tweepy import API, OAuthHandler,Cursor
from textblob import TextBlob
from ....db_con import database_setup
import io
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib import pyplot as plt
import base64
import numpy as np

import uuid

class Twitter():

    def __init__(self):
        self.database = database_setup()
        self.cursor = self.database.cursor

        self.auth = self.authenticate_twitter_app()
        self.twitter_client = API(self.auth)
        self.twitter_user = None


    def authenticate_twitter_app(self):
        auth = OAuthHandler('r7fHaRwhccxQXFuN9nmQCHYiI', 'T2A5Sxs1rHyx5P1HgFDnQ5VQd7tXPv0DEsFEYjLCojEsgJlThx')
        auth.set_access_token('1005899876742377474-WuxZRYNt3dwEM62D4gCrnZEW6vtnKo', 'IBxDDAVK7ptPumqxeslnUR6TfLpVT1CpXBgQzEfXGNgnA')
        return auth



    def get_twitter_client_api(tweet,self):
        return self.twitter_client


    def percentage(self,part,whole):
        return 100 * float(part) /float(whole)


    def tweet_analysis(self,topic,num_tweets):
        tweets = self.twitter_client.search(topic, tweet_mode='extended')

        positive = 0
        negative = 0
        neutral = 0
        polarity = 0

        for tweet in tweets:
            analysis = TextBlob(tweet.full_text)
            polarity += analysis.sentiment.polarity
            if(analysis.sentiment.polarity == 0):
                neutral += 1
            elif(analysis.sentiment.polarity < 0.00):
                negative += 1
            elif(analysis.sentiment.polarity > 0.00):
                positive += 1


        positive = self.percentage(positive,num_tweets)
        negative = self.percentage(negative,num_tweets)
        neutral = self.percentage(neutral,num_tweets)


        if(polarity == 0):
            weight = 'neutral'
        elif(polarity < 0):
            weight = 'negative'
        elif(polarity > 0):
            weight = 'positive'

        return(positive,negative,neutral)



    def plot_pie(self,topic,num_tweets):

        cent = self.tweet_analysis(topic,num_tweets)
        positive = cent[0]
        neutral = cent[1]
        negative = cent[2]

        positive = format(positive, '.2f')
        negative = format(negative, '.2f')
        neutral = format(neutral, '.2f')

        labels = ['Positive ['+ str(positive) + '%]','Neutral ['+ str(neutral) + '%]','Negative ['+ str(negative) + '%]']
        sizes = [positive,neutral,negative]
        colors = ['yellowgreen','gold','red']
        patches,text = plt.pie(sizes,colors=colors,startangle=90)
        plt.legend(patches,labels,loc='best')
        plt.title('How people are reacting to '+topic+' by analyzing '+str(num_tweets)+' Tweets.' )
        plt.axis('equal')
        plt.tight_layout()
        pname = str(uuid.uuid4())
        plt.savefig('app/static/img/plot/'+pname+'.png')
        plt.close('all')
        plt.clf()
        return pname



    def plot_bar(self,topic,num_tweets):
        cent = self.tweet_analysis(topic,num_tweets)
        colors = ['yellowgreen','gold','red']

        label = ['positive','neutral','negative']
        y_pos = np.arange(len(label))
        results = [cent[0],cent[1],cent[2]]

        plt.bar(y_pos,results,color=colors,align='center', alpha=0.5)
        plt.xticks(y_pos,label)
        plt.ylabel('Percentage')
        plt.xlabel('Sentiment')
        plt.title('How people are reacting to '+topic+' by analyzing '+str(num_tweets)+' Tweets.' )
        bname = str(uuid.uuid4())
        plt.savefig('app/static/img/plot/'+bname+'.png')
        plt.clf()

        return bname


    def add_report(self,tweet,num_tweet,email,pie,bar):

        report = {
            "tweet": tweet,
            "num_tweet": num_tweet,
            "email": email,
            "bar":bar,
            "pie": pie
        }

        query = """INSERT INTO Report (tweet,num_tweet,plot_bar,plot_pie,email)
            VALUES(%(tweet)s,%(num_tweet)s,%(bar)s, %(pie)s,%(email)s);"""
        self.cursor.execute(query, report)
        self.database.conn.commit()

        return report

    def get_reports(self):
        self.cursor.execute("SELECT * from report ORDER BY report_id DESC;")
        query = self.cursor.fetchall()

        return query


    def get_report(self,report_id):
        self.cursor.execute("SELECT * from report where report_id= '%s';" % (report_id))
        query = self.cursor.fetchall()

        return query

    def remove_report(self,report_id):
        query = "DELETE FROM report WHERE report_id = '%s';" % (report_id)
        self.cursor.execute(query)

        self.database.conn.commit()


    def update_config(self,consumerKey,consumerSecret,accessToken,accessSecret,email):

        report = {
            "consumerKey": consumerKey,
            "consumerSecret": consumerSecret,
            "accessToken":  accessToken,
            "accessSecret":accessSecret,
            "email": email
        }

        query = "UPDATE Config SET consumerKey='%s',consumerSecret='%s',accessToken='%s',accessSecret='%s' WHERE email = '%s';" % (consumerKey,consumerSecret,accessToken,accessSecret,email)
        self.cursor.execute(query, report)
        self.database.conn.commit()

        return report










