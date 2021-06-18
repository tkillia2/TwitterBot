import tweepy
import datetime
import os
import requests
import cryptocompare
import time

#import reddit.py
#import Tkinter


consumer_key = 'Rzrjeug9nqq0lIL9XPp48V9Ab'
consumer_secret = 'QbWa2w8WSMy5pfuTAkXnWLZGcIWjppAY46r69vD8ZI9RXp4fKz'

access_token = '1404473074234372099-y8uChSmEpfr2QV5f1OoOE7tDTzIzzG'
access_token_secret = 'jBYUwm7Ga0wlQ94gHHQR6uACsCQsc3i919cDqhCbg0svY'

## Auhtorize the account
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

## Sets me as the user and then lets me check if it is connected by printing my name
user = api.me()
print(user.name)

# Follows everyone back who follows me!
"""
I guess this violates twitter's following rules? got banned for three days??
for follower in tweepy.Cursor(api.followers).items():
    follower.follow()
print("Followed everyone that is following " + user.name)
"""

# Function to retrieve the timeline
def retrieve_timeline( api, user ):
    return api.user_timeline(screen_name = user, include_rts = True)

# gets the current time
CURRENT_TIME = datetime.datetime.utcnow()# - datetime.timedelta(30)
"""
# User name for possible user you want to favorite, retweet, or quote tweet
USER_NAME = "tcostigan33"

# Possible message if you want it consistent 
message = "hey check out this cool bot thing"

# create api object
api = tweepy.API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify = True)

#grab current timeline
user_tweets = retrieve_timeline(api, USER_NAME)

## Allows you to automate dming a certain person
DM_NAME = "tcostigan33"
dm_id = api.get_user(DM_NAME)
dm_user = dm_id.id_str
api.send_direct_message(dm_user, "hello user")

# This does in fact tweet this out on your account
api.update_status("Did it work this time")

#run through tweets and retweets
for tweet in user_tweets:
    #time_obj = datetime.datetime.strptime(tweet._json['created_at'][4:],"%b %d %H:%M:%S %z %Y" )
    if "RT" in tweet._json['text']:
        # Prints out whatever the user has retweeted
        print(f"{tweet._json['user']['name']} retweeted {tweet._json['text'][2:]} at {tweet._json['created_at']}")
    else:
        # Replies to the user
        api.update_status("@" + USER_NAME + " awesome tweet", in_reply_to_status_id = tweet.id)
        # Retweets and favorites the user's tweet
        tweet.retweet()
        tweet.favorite()

        # Prints out whatever they tweeted just like above
        #print(f"{tweet._json['user']['name']} tweeted {tweet._json['text']} at {tweet._json['created_at']}")

response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
data = response.json()
btc = data["bpi"]["USD"]["rate"]
api.update_status(f"Bitcoin's current price: {btc} (USD) \n\t Prices obtained from: https://www.coindesk.com/price/\
bitcoin\n\t Powered by CoinDesk")
"""
btc = cryptocompare.get_price('BTC', currency = 'USD')['BTC']
"""
try:
    api.update_status(f"Bitcoin's current price: {btc['USD']} (USD) #Bitcoin #Crypto #BTC")
except:
    tweepy.TweepError
"""
eth = cryptocompare.get_price('ETH', currency = 'USD')['ETH']
"""
try:
    api.update_status(f"Ethereum's current price: {eth['USD']} (USD) #Ethereum #Crypto #ETH")
except:
    tweepy.TweepError
"""
doge = cryptocompare.get_price('DOGE', currency = 'USD')['DOGE']
"""
try:
    api.update_status(f"Dogecoin's current price: {doge['USD']} (USD) #Dogecoin #Crypto #DOGE")
except:
    tweepy.TweepError
"""
safemoon = cryptocompare.get_price('SAFEMOON', currency = 'USD')['SAFEMOON']
"""
try:
    api.update_status(f"Safemoon's current price: {safemoon['USD']} (USD) #Safemoon #Crypto #SAFEMOON")
except:
    tweepy.TweepError
"""
try:
    api.update_status(f"\tBitcoin Price (USD): {btc['USD']} \nEthereum Price (USD): {eth['USD']} \nDogecoin Price (USD): {doge['USD']} \nSafemoon Price (USD): {safemoon['USD']} \n#Bitcoin #Dogecoin #Ethereum #Safemoon #Crypto")
except:
    tweepy.TweepError

time.sleep(900)
"""
search = "What is Bitcoin's price"
numberOfTweets = 5
phrase = f"Bitcoin's current price: {btc['USD']} (USD) #Bitcoin"
for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
    try:
        tweetId = tweet.user.id
        username = tweet.user.screen_name
        api.update_status("@" + username + " " + phrase, in_reply_to_status_id = tweet.id)
        print ("Replied with " + phrase)

    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
"""
"""

Chunk of Code will search for the given item word and retweet the number of tweets you want 
that contains that word  -- code found on medium.com/free-code-camp/creating-a-twitter-bot...

search = "Crypto"
numberOfTweets = 1
for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
    try:
        tweet.retweet()
        print('Retweeted the tweet')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
search = "Ethereum"
numberOfTweets = 1
for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
    try:
        tweet.retweet()
        print('Retweeted the tweet')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
search = "Dogecoin"
numberOfTweets = 1
for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
    try:
        tweet.retweet()
        print('Retweeted the tweet')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
search = "Safemoon"
numberOfTweets = 1
for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
    try:
        tweet.retweet()
        print('Retweeted the tweet')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
"""
