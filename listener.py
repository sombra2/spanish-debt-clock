# this is the listening script for users retweeting and new follows

import tweepy
import credentials

consumer_key = credentials.consumer_key
consumer_secret = credentials.consumer_secret
access_token = credentials.access_token
access_token_secret = credentials.access_token_secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create API object
api = tweepy.API(auth)

# Create stream listener
class MyStreamListener(tweepy.Stream):
    def on_follow(self, follower):
        # Send tweet to new follower
        api.update_status(f"Gracias por seguirnos, @{follower.screen_name}!")

# Create stream object and start listening
myStreamListener = MyStreamListener(auth = api.auth)
myStreamListener.filter(track=["@your_bot_name"])

# Get recent tweets and their retweets
tweets = api.user_timeline(screen_name="your_bot_name", count=20, include_rts=True)

# Like retweets
for tweet in tweets:
    retweets = api.retweets(tweet.id)
    for retweet in retweets:
        api.create_favorite(retweet.id)