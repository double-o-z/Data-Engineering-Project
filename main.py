import tweepy

with open('twitter_key.txt', 'r') as fp:
    consumer_key, consumer_secret = fp.read().split(",")

auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)
api = tweepy.API(auth)

for tweet in tweepy.Cursor(api.search, q='israel lockdown').items(10):
    print(tweet.text)
