import tweepy
import datetime
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
for follower in tweepy.Cursor(api.followers).items():
    follower.follow()
print("Followed everyone that is following " + user.name)

# Function to retrieve the timeline
def retrieve_timeline( api, user ):
    return api.user_timeline(screen_name = user, include_rts = True)

# gets the current time
CURRENT_TIME = datetime.datetime.utcnow()# - datetime.timedelta(30)

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

