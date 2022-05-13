import tweepy
import os
import threading
import time
import random
import requests
from binance import Client
from bs4 import BeautifulSoup
from dotenv import load_dotenv

#ENV setup
#base directory the file is in
BASEDIR = os.path.abspath(os.path.dirname(__file__))

#join base directory with filename
load_dotenv(os.path.join(BASEDIR, '.env'))

#binance setup
def get_price(coin):
    api_key = os.getenv('API_KEY')
    api_secret = os.getenv('BINANCE_SECRET_KEY')

    client = Client(api_key, api_secret)
    coin_price = client.get_symbol_ticker(symbol=coin)
    return coin_price['price']

#twitter set up
def create_api():

    consumer_key = os.getenv('CONSUMER_KEY')
    consumer_secret = os.getenv('CONSUMER_SECRET')
    access_token = os.getenv('ACCESS_TOKEN')
    access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    try:
        api.verify_credentials()
        print("Authentication successful")
        return api
    except:
        print("error")

def tweet_price():
    api = create_api()
    bitcoin = get_price("BTCUSDT")
    ethereum = get_price("ETHUSDT")
    
    tweet = "here are the prices for today: \n" + "bitcoin: $" + bitcoin + "\n" + "ethereum: $" + ethereum + "\n"

    threading.Timer(86400.0, tweet_price).start() #tweet every 24hrs
    
    api.update_status(tweet)

    print("message has been tweeted")

tweet_price()