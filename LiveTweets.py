import json
import sys
#import tweepy
from tweepy import OAuthHandler, Stream
from tweepy.streaming import StreamListener

class TweetStreamListener(StreamListener):
    def on_data(self, data):
        tweet = json.loads(data)
        if "created_at" in tweet:
            print( tweet["created_at"][4:-10] + " " + tweet["text"][:70] + "\n")
        return True
    
    def on_error(self, status):
        print(status)

with open('auth.k','r') as authfile:
        ak = authfile.readlines()

consumer_key, consumer_secret = ak[0].strip(), ak[1].strip()
access_key, access_secret = ak[2].strip(), ak[3].strip()

auth_key = OAuthHandler(consumer_key, consumer_secret)
auth_key.set_access_token(access_key, access_secret)

#query = input("Enter keyword")

try:
    listener = TweetStreamListener()
    live_twitter_stream = Stream(auth_key, listener)
    live_twitter_stream.filter(track=[sys.argv[1]])
except KeyboardInterrupt as e:
    sys.exit()
