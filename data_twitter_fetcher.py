import tweepy
import time
import random


consumer_key="fYNRbw6298ZgHDpViRPFmslxz"
consumer_secret="GZ6DHTjOB5T6nDrHjEdxO9YzsIrPq6haHYXdgNUqMPQYGQtbET"
Access_key="923299188938592256-T0pvmmFs34PPFYovrHSFkBODfkhyogY"
Access_secret="DVj6Ytg1yP7U2ikJqyaPrABQR8BKUu8Rue2l1x1niwJ66"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret) #tweet module name.Outhstuff(cons_key, secret_key)
auth.set_access_token(Access_key, Access_secret)
api = tweepy.API(auth)

def mentions():
    
    (pub_tweets) = api.mentions_timeline()
    for tweet in pub_tweets:
        twee = tweet.__dict__
        print(twee)
#smt = bool        
inpu = input("")
while inpu == "y":
    if inpu == "y":
        mentions()
        
    #break smt == bool(inpu)
    else:
        print("type again")

