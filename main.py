import requests
from dotenv import load_dotenv
import os
import json

from Twitter import Twitter

load_dotenv()
twitter = Twitter()

DEEP_API_KEY = os.getenv("DEEP_API_KEY")

twitter_user = input("Enter twitter username: ")

latest_tweet = twitter.get_tweet(twitter_user)

print(latest_tweet)

r = requests.post(
    "https://api.deepai.org/api/sentiment-analysis",
    data={
        'text': f'{latest_tweet}',
    },
    headers={
        'api-key': DEEP_API_KEY
    }
)
print(r.json())
