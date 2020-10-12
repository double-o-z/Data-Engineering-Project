import pandas as pd
from tabulate import tabulate
import tweepy as tw

with open('twitter_key.txt', 'r') as fp:
    consumer_key, consumer_secret, access_token, access_token_secret = fp.read().split(",")

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

# tweets_cursor = tw.Cursor(
#     api.search,
#     lang="en",
#     q='israel lockdown',
#     since="2020-09-18").items(100)
# for tweet in tweets:
#     print(tweet.text)
# tweets = [tweet.text for tweet in tweets_cursor]
tweets = [tweet.text for tweet in api.home_timeline()]

tweet_text = pd.DataFrame(data=tweets, columns=["text"])
print("Tweet text table :\n" + tweet_text.to_markdown())
