import tweepy
import os
import threading
import time
import random
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

#ENV setup
#base directory the file is in
BASEDIR = os.path.abspath(os.path.dirname(__file__))

#join base directory with filename
load_dotenv(os.path.join(BASEDIR, '.env'))

def search_price(coin):
    url = "https://www.google.com/search?q="+coin+"+price"
    get_html = requests.get(url)
    parse = BeautifulSoup(get_html.text, 'lxml')
    text = parse.find("div", attrs={'class':'BNeawe iBp4i AP7Wnd'}).find("div", attrs={'class':'BNeawe iBp4i AP7Wnd'}).text

    print(text)
    return text


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

#Loop works but still throws an error due to duplicate status tweet
#Todo implement a way to tweet different things on server

def tweet_price():
    api = create_api()
    bitcoin = search_price("bitcoin")
    litecoin = search_price("litecoin")
    cardano = search_price("cardano")
    doge = search_price("doge")
    
    tweet = "here are the prices for today: \n" + "bitcoin: " + bitcoin + "\n" + "litecoin: " + litecoin + "\n" + "cardano: " + cardano + "\n" + "doge: " + doge + "\n"

    threading.Timer(86400.0, tweet_price).start() #tweet every 24hrs
    
    api.update_status(tweet)

    print("message has been tweeted")

tweet_price()

