import unittest
import Twitter
from Twitter import Twitter

class TestTwitterMethods(unittest.TestCase):

    def test_get_tweets_user(self):
        twitter = Twitter()
        user = '@twitter'
        result = twitter.get_tweets(user)
        self.assertIsInstance(result, list)

    def test_get_tweets_search(self):
        twitter = Twitter()
        search_term = 'news'
        result = twitter.get_tweets(search_term)
        self.assertIsInstance(result, list)

    def test_get_tweets_hashtag(self):
        twitter = Twitter()
        hashtag = '#news'
        result = twitter.get_tweets(hashtag)
        self.assertIsInstance(result, list)

    def test_parse_tweets(self):
        twitter = Twitter()
        tweets = twitter.get_tweets('@twitter')
        parsed_tweets = twitter.parse_tweets(tweets)
        self.assertIsInstance(parsed_tweets, str)

if __name__ == '__main__':
    unittest.main()
