import requests
from dotenv import load_dotenv  # type: ignore
import os
import re

load_dotenv()

BEARER_TOKEN = os.getenv("BEARER_TOKEN")


class Twitter():
    @classmethod
    def get_tweets(cls, search_term: str) -> list:
        """Request tweets from Twitter API using search term provided by user.

        Args:
            search_term (str): String input is the search term provided by user

        Returns:
            list: A list of dictionaries of each tweet provided by Twitter API
        """
        try:
            if search_term[0] == '@':
                query = f"from:{search_term[1:]}"
            elif search_term[0] == '#':
                query = f"%23{search_term[1:]}"
            else:
                search_term = search_term.replace('/', '%20')
                search_term = search_term.replace(' ', '%20')
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
        """Takes each tweet from a list of tweets retrieved from
        get_tweets method and parses them into a single string.
        Just the text content from each tweet is taken, and any
        links are removed.

        Args:
            tweets (list): List of tweets retrieved from get_tweets method

        Returns:
            str: The text of all the strings of each tweet
            joined with '. ' and all links removed
        """
        tweet_text = ''

        for tweet in tweets:
            links_removed = re.sub(r'http\S+',
                                   '', tweet['text'], flags=re.MULTILINE)
            tweet_text += links_removed + '. '

        return tweet_text
