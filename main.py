from Twitter import Twitter
from Analysis import Analysis

twitter = Twitter()
analysis = Analysis()

twitter_user = input("Enter twitter username or search query: ")

latest_tweets = twitter.get_tweets(twitter_user)

if latest_tweets:
    analysis.analyse_text(latest_tweets)
