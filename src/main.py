import requests
from dotenv import load_dotenv
import os
import json

load_dotenv()

BEARER_TOKEN = os.getenv("BEARER_TOKEN")
DEEP_API_KEY = os.getenv("DEEP_API_KEY")

twitter_user = input("Enter twitter username: ")

query = f"from:{twitter_user}"

tweet_fields = "tweet.fields=author_id"

url = f"https://api.twitter.com/2/tweets/search/recent?query={query}&{tweet_fields}"

headers = {"Authorization": "Bearer {}".format(BEARER_TOKEN)}

response = requests.get(url, headers=headers)
latest_tweet = json.loads(response.text)['data'][0]['text']

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
