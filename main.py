import requests
from dotenv import load_dotenv
import os

from Twitter import Twitter

load_dotenv()
twitter = Twitter()

DEEP_API_KEY = os.getenv("DEEP_API_KEY")

twitter_user = input("Enter twitter username: ")

latest_tweets = twitter.get_tweets(twitter_user)

print(latest_tweets)

r = requests.post(
    "https://api.deepai.org/api/sentiment-analysis",
    data={
        'text': f'{latest_tweets}',
    },
    headers={
        'api-key': DEEP_API_KEY
    }
)
print(r.json())
