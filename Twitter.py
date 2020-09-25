import requests
from dotenv import load_dotenv  # type: ignore
import os

load_dotenv()

BEARER_TOKEN = os.getenv("BEARER_TOKEN")

class Twitter():
    @classmethod
    def get_tweets(cls, twitter_id):
        try:
            if twitter_id[0] == '@':
                query = f"from:{twitter_id[1:]}"
            else:
                query = f"{twitter_id}, lang:en"
            url = f"https://api.twitter.com/2/tweets/search/recent?query={query}&max_results=50&tweet.fields=text"
            headers = {"Authorization": f"Bearer {BEARER_TOKEN}"}

            response = requests.get(url, headers=headers)
            if response.json()['meta']['result_count'] == 0:
                print("There were no tweets to retrieve for that input.")
                return None
            else:
                return response.json()['data']
        except:
            print(Exception)
            print("Sorry, looks like something went wrong!")

    @classmethod
    def parse_tweets(cls, tweets):
        tweet_text = ''

        for tweet in tweets:
            tweet_text += tweet['text'] + '. '

        return tweet_text