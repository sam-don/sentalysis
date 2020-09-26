import unittest
import Twitter
from Twitter import Twitter

class TestTwitterMethods(unittest.TestCase):
    def test_tests_running(self):
        self.assertTrue(True)

    def test_get_tweets_user(self):
        twitter = Twitter()
        user = '@twitter'
        result = twitter.get_tweets(user)
        self.assertIsInstance(result, list)

    def test_parse_tweets(self):
        twitter = Twitter()
        tweets = twitter.get_tweets('@twitter')
        parsed_tweets = twitter.parse_tweets(tweets)
        self.assertIsInstance(parsed_tweets, str)

if __name__ == '__main__':
    unittest.main()
