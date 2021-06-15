import tweepy
import datetime
#import Tkinter


consumer_key = 'wNpBZP70RBB29JVsTsnYYG4nX'
consumer_secret = 'iW9hXzNVnkAs3LXoxo7xQvJvPBny3iLSXCzn0P7xHMwj0cvhoE'

access_token = '1404473074234372099-4LeZJqFjO17JXCROUs9apQrNxDgdRp'
access_token_secret = 'DTbsS1jHixwToEwb1PEQVrdUpU9lVnkoBomTx6SDA4u0R'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

user = api.me()
print(user.name)

for follower in tweepy.Cursor(api.followers).items():
    follower.follow()
    print("Followed everyone that is following " + user.name)

def retrieve_timeline( api, user ):
    return api.user_timeline(screen_name = user, include_rts = True)

CURRENT_TIME = datetime.datetime.utcnow()# - datetime.timedelta(30)

#SEAN_NAME = "seanrubey15"
message = "hello sean"
# create api object
api = tweepy.API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify = True)

# grab current timeline
#sean_tweets = retrieve_timeline(api, SEAN_NAME)

#toReply = "seanrubey15" #user to get most recent tweet
#api = tweepy.API(auth)

#dm_id = api.get_user(SEAN_NAME)
#dm_user = user.id_str
#api.send_direct_message(dm_user, "hello sean rubey")

#get the most recent tweet from the user
#tweets = api.user_timeline(screen_name = toReply, count=11)
#api.update_status(" HELLO @seanrubey15 check out this awesome link!! https://www.youtube.com/watch?v=XS7JElb-Jps")

#for tweet in tweets:
#    api.update_status("@" + toReply + " Wow that is so awesome Sean!", in_reply_to_status_id = tweet.id)
count = 0
while count < 10:
    api.update_status("new tweet")
    count += 1
"""
#run through tweets and retweets
for tweet in sean_tweets:
    #time_obj = datetime.datetime.strptime(tweet._json['created_at'][4:],"%b %d %H:%M:%S %z %Y" )
    if "RT" in tweet._json['text']:
        #api.update_status("@seanrubey15 this is great, keep up the good work", in_reply_to_status_id = tweet.id)
        print(f"{tweet._json['user']['name']} retweeted {tweet._json['text'][2:]} at {tweet._json['created_at']}")
    else:
        api.update_status("@" + SEAN_NAME + " super funny dude, keep up the good work", in_reply_to_status_id = tweet.id)
        #tweet.retweet()
        #tweet.favorite()
        #api.send_direct_message(dm_user, "hey baby")
        #tweet.unretweet()
        #tweet.unfavorite()
        #tweet.retweet()
        #print(f"{tweet._json['user']['name']} tweeted {tweet._json['text']} at {tweet._json['created_at']}")

#api.send_direct_message(SEAN_NAME, message)
"""
