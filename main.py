from Twitter import Twitter
from Analysis import Analysis

twitter = Twitter()
analysis = Analysis()

running = True

while running:

    twitter_user = input("Enter twitter username or search query: ")

    latest_tweets = twitter.get_tweets(twitter_user)
    if latest_tweets == None:
        continue
    
    parsed_tweets = twitter.parse_tweets(latest_tweets)

    analysis.analyse_text(parsed_tweets)
