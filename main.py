import requests
from dotenv import load_dotenv  # type: ignore
import os

from Twitter import Twitter

load_dotenv()
twitter = Twitter()

DEEP_API_KEY = os.getenv("DEEP_API_KEY")

twitter_user = input("Enter twitter username or search query: ")

latest_tweets = twitter.get_tweets(twitter_user)

if latest_tweets:

    r = requests.post(
        "https://api.deepai.org/api/sentiment-analysis",
        data={
            'text': latest_tweets,
        },
        headers={
            'api-key': DEEP_API_KEY
        }
    )

    sentiments = r.json()['output']

    total = len(sentiments)

    neutral = sentiments.count('Neutral')
    positive = sentiments.count('Positive')
    negative = sentiments.count('Negative')

    print(f'''
    Sentiment Analysis
    ------------------

    Total phrases analysed: {total}

    {positive} positive phrases, {(positive / total * 100):.2f}%
    {neutral} neutral phrases, {(neutral / total * 100):.2f}%
    {negative} negative phrases, {(negative / total * 100):.2f}%


    ''')
