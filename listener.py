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
        api.update_status(f"Thanks for following, @{follower.screen_name}!")

# Create stream object and start listening
myStreamListener = MyStreamListener(
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token=access_token,
    access_token_secret=access_token_secret
)
myStreamListener.filter(follow=[api.get_user("your_bot_name").id_str], is_async=True)

# Get recent tweets and their retweets
tweets = api.user_timeline(screen_name="your_bot_name", count=20, include_rts=True)

# Like retweets
for tweet in tweets:
    retweets = api.retweets(tweet.id)
    for retweet in retweets:
        api.create_favorite(retweet.id)