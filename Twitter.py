import requests
from dotenv import load_dotenv  # type: ignore
import os
import re

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
                search_term = search_term.replace('/', '%20')
                search_term = search_term.replace(' ', '%20')
                print(search_term)
                query = f"{search_term}, lang:en"
            url = f"https://api.twitter.com/2/tweets/search/recent?query=\
            {query}&max_results=50&tweet.fields=text"
            headers = {"Authorization": f"Bearer {BEARER_TOKEN}"}

            response = requests.get(url, headers=headers)
            if response.json()['meta']['result_count'] == 0:
                print("There were no tweets to retrieve for that input.")
                return []
            else:
                return response.json()['data']
        except Exception:
            print("Sorry, looks like something went wrong!")
            return []

    @classmethod
    def parse_tweets(cls, tweets: list) -> str:
        tweet_text = ''

        for tweet in tweets:
            links_removed = re.sub(r'http\S+',
                                   '', tweet['text'], flags=re.MULTILINE)
            tweet_text += links_removed + '. '

        return tweet_text
