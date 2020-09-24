import requests
from dotenv import load_dotenv
import os
import json

load_dotenv()

BEARER_TOKEN = os.getenv("BEARER_TOKEN")

class Twitter():
    @classmethod
    def get_tweet(cls, twitter_id):
        try:
            query = f"from:{twitter_id}"
            tweet_fields = "tweet.fields=author_id"
            url = f"https://api.twitter.com/2/tweets/search/recent?query={query}&{tweet_fields}"
            # headers = {"Authorization": "Bearer {}".format(BEARER_TOKEN)}
            headers = {"Authorization": f"Bearer {BEARER_TOKEN}"}

            response = requests.get(url, headers=headers)
            latest_tweet = json.loads(response.text)['data'][0]['text']

            return latest_tweet
        except Exception:
            return None
