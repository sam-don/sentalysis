from Twitter import Twitter
from Analysis import Analysis

twitter = Twitter()
analysis = Analysis()

running = True

while running:

    twitter_user = input("Enter twitter username or search query: ")

    latest_tweets = twitter.get_tweets(twitter_user)
    if latest_tweets == []:
        continue

    parsed_tweets = twitter.parse_tweets(latest_tweets)

    deep_ai_data = analysis.analyse_text(parsed_tweets)
    if deep_ai_data == []:
        continue

    analysed_data = analysis.collate_data(deep_ai_data)

    analysis.view_report(analysed_data)
