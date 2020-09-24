import requests
import os
import json

BEARER_TOKEN = os.getenv("BEARER_TOKEN")

class Twitter():
    @classmethod
    def get_tweets(cls, twitter_id):
        try:
            query = f"from:{twitter_id}"
            url = f"https://api.twitter.com/2/tweets/search/recent?query={query}"
            headers = {"Authorization": f"Bearer {BEARER_TOKEN}"}

            response = requests.get(url, headers=headers)
            tweets = json.loads(response.text)['data']

            print(tweets)

            tweet_text = ''

            for tweet in tweets:
                tweet_text += tweet['text'] + '. '

            return tweet_text
        except Exception:
            return None
