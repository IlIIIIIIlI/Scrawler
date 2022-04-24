import tweepy
import configparser

# read configs
config = configparser.ConfigParser()
config.read("config.ini")

api_key = config["twtter"]["api_key"]
api_key_secret = config["twtter"]["api_key_secret"]
access_token = config["twtter"]["access_token"]
access_token_secret = config["twtter"]["access_token_secret"]

# authentication
auth = tweepy.OAuthHandler(api_key, api_key_secret)

auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_twts = api.home_timeline()
pirnt(public_twts)
