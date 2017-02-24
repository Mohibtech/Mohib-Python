# encoding: utf-8
import tweepy  # pip install tweepy
import csv

def authTwitter():               
        #Create auth.k file with consumer key, secret and access key , secret as simple text file and read it here
        with open('auth.k','r') as authfile:   
                ak = authfile.readlines()

        consumer_key, consumer_secret = ak[0].strip(), ak[1].strip()
        access_key, access_secret = ak[2].strip(), ak[3].strip()
        
        auth1 = tweepy.auth.OAuthHandler(consumer_key, consumer_secret)
        auth1.set_access_token(access_key, access_secret)
        return tweepy.API(auth1)

def get_all_tweets(screen_name, alltweets=[], max_id=0):
        # Twitter only allows access to a users most recent 3240 tweets with this method authorize twitter, initialize tweepy
    api = authTwitter()

    # make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.user_timeline(screen_name=screen_name, count=200)

    # save most recent tweets
    alltweets.extend(new_tweets)

    # save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1

    # keep grabbing tweets until there are no tweets left to grab
    while len(new_tweets) > 0:

        # all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(screen_name=screen_name, count=200, max_id=oldest)

        # save most recent tweets
        alltweets.extend(new_tweets)

        # update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1

        print("...%s tweets downloaded so far" % (len(alltweets)))


    return alltweets

def write_csv_file(retTweets, screen_name):
    # transform the tweepy tweets into a 2D array that will populate the csv
    outtweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in retTweets]
    
    # write the csv
    with open('%s_tweets.csv' % screen_name, 'w', encoding='utf8') as f:
        writer = csv.writer(f)
        writer.writerow(["id", "created_at", "text"])
        writer.writerow(outtweets)

if __name__ == '__main__':
    # pass in the username of the account you want to download
    screen_name = "mohibawan"
    retTweets = get_all_tweets(screen_name, [], 0)

    write_csv_file(retTweets, screen_name)
