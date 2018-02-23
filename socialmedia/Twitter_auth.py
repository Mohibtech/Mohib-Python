#Import the necessary methods from tweepy library
import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#provide your access details below
access_token = "73738586-..."
access_token_secret = "vd.."
consumer_key = "1f..."
consumer_secret = "H.."

# establish a connection
auth = tweepy.auth.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#Let’s assume that you would like to understand what is being said about the iPhone 7 and its camera feature. So let’s pull the most recent 10 posts.
# You can pull historic user posts about a topic for a max of 10 to 15 days only, depending on the volume of the posts.
#fetch recent 10 tweets containing words iphone7, camera

fetched_tweets = api.search(q=['iPhone 7','iPhone7','camera'], result_type='recent', lang='en', count=10)
print ("Number of tweets: ",len(fetched_tweets) )
