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
            'text': f'{latest_tweets}',
        },
        headers={
            'api-key': DEEP_API_KEY
        }
    )

sentiments = r.json()['output']

neutral = sentiments.count('Neutral')
positive = sentiments.count('Positive')
negative = sentiments.count('Negative')

print(f'''
Sentiment Analysis
------------------

Neutral: {neutral}
Positive: {positive}
Negative: {negative}
''')