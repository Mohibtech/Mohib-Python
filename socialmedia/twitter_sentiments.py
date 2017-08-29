# -*- coding: utf-8 -*-
import csv
import tweepy
import unidecode as ud

# Twitter auth.k file format
'''
consumer_key
consumer_secret
access_key
access_secret
'''

def authTwitter():               
        with open('auth.k','r') as authfile:
                ak = authfile.readlines()

        consumer_key, consumer_secret = ak[0].strip(), ak[1].strip()
        access_key, access_secret = ak[2].strip(), ak[3].strip()
        
        auth1 = tweepy.auth.OAuthHandler(consumer_key, consumer_secret)
        auth1.set_access_token(access_key, access_secret)
        return tweepy.API(auth1)

api = authTwitter()

with open('test1_tweets.csv', 'w', encoding='utf8') as csvTweets:
    csvWriter = csv.writer(csvTweets)
    col_header = ['username','author id','created', 'text', 'retwc', 'hashtag', 'followers', 'friends']
    csvWriter.writerow(col_header)

    for t in tweepy.Cursor(api.search, q="urdu", lang="en", result_type="popular", count=10).items():
        text = ud.unidecode(t.text)
        try:
            hashtag = tweet.entities[u'hashtags'][0][u'text'] #hashtags used
        except:
            hashtag = "None"
        
        row = [t.author.name, t.author.id , t.created_at, text, t.retweet_count, hashtag, t.author.followers_count, t.author.friends_count]
        csvWriter.writerow(row)
