import requests
from dotenv import load_dotenv  # type: ignore
import os

load_dotenv()

BEARER_TOKEN = os.getenv("BEARER_TOKEN")

class Twitter():
    @classmethod
    def get_tweets(cls, search_term: str) -> list:
        try:
            if search_term[0] == '@':
                query = f"from:{search_term[1:]}"
            elif search_term[0] == '#':
                query = f"%23{search_term[1:]}"
            else:
                query = f"{search_term}, lang:en"
            url = f"https://api.twitter.com/2/tweets/search/recent?query={query}&max_results=50&tweet.fields=text"
            headers = {"Authorization": f"Bearer {BEARER_TOKEN}"}

            response = requests.get(url, headers=headers)
            if response.json()['meta']['result_count'] == 0:
                print("There were no tweets to retrieve for that input.")
                return []
            else:
                return response.json()['data']
        except:
            print("Sorry, looks like something went wrong!")
            return []

    @classmethod
    def parse_tweets(cls, tweets: list) -> str:
        tweet_text = ''

        for tweet in tweets:
            tweet_text += tweet['text'] + '. '

        return tweet_text