import tweepy
import os
import threading
from dotenv import load_dotenv
#import bs4
#import requests
#import re
import threading

#base directory the file is in
BASEDIR = os.path.abspath(os.path.dirname(__file__))

#join base directory with filename
load_dotenv(os.path.join(BASEDIR, '.env'))

consumer_key = os.getenv('CONSUMER_KEY')
consumer_secret = os.getenv('CONSUMER_SECRET')
access_token = os.getenv('ACCESS_TOKEN')
access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)



#Loop works but still throws an error due to duplicate status tweet
#Todo implement a way to tweet different things on server
def tweet_stuff():
    try:
        api.verify_credentials()
        print("Authentication successful")
    except:
        print("error")

    threading.Timer(60.0, tweet_stuff).start()
    
    api.update_status('pain.')
    print("message has been tweeted")

tweet_stuff()