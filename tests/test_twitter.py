import unittest
import Twitter
from Twitter import Twitter

class TestTwitterMethods(unittest.TestCase):

    def setUp(self):
        self.twitter = Twitter()

    def test_get_tweets_user(self):
        """Test if retrieving specific user tweets returns list correctly.
        This test will return an empty list and should still pass if 
        there is no Twitter Bearer Token available.
        """
        user = '@twitter'
        result = self.twitter.get_tweets(user)
        self.assertIsInstance(result, list)

    def test_get_tweets_search(self):
        """Test if retrieving tweets for a generic search term returns list correctly.
        This test will return an empty list and should still pass if 
        there is no Twitter Bearer Token available.
        """
        search_term = 'news'
        result = self.twitter.get_tweets(search_term)
        self.assertIsInstance(result, list)

    def test_get_tweets_hashtag(self):
        """Test if retrieving specific hashtag tweets returns list correctly.
        This test will return an empty list and should still pass if 
        there is no Twitter Bearer Token available.
        """
        hashtag = '#news'
        result = self.twitter.get_tweets(hashtag)
        self.assertIsInstance(result, list)

    def test_parse_tweets(self):
        """Test if a list of tweets correctly parses into a single string.
        """
        tweets = self.twitter.get_tweets('@twitter')
        parsed_tweets = self.twitter.parse_tweets(tweets)
        self.assertIsInstance(parsed_tweets, str)
