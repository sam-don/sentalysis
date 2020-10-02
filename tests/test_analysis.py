import unittest
import Analysis
from Analysis import Analysis

class TestAnalysisMethods(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.analysis = Analysis()

    def test_analyse_text(self):
        """Test if retrieving specific user tweets returns list correctly.
        This test will return an empty list and should still pass if 
        there is no Twitter Bearer Token available.
        """
        test_input = "This is some text to analyse.\
             If a Deep AI API Key is not available to use it will return an empty list."
        result = self.analysis.analyse_text(test_input)
        self.assertIsInstance(result, list)

    def test_collate_data(self):
        """Given a list of strings as input, return a dict with the correct values.
        This test will return an empty list and should still pass if 
        there is no Deep AI API Key available.
        """
        test_input = ['Neutral', 'Neutral', 'Positive', 'Neutral', 'Verynegative', 'Positive', 'Negative', 'Verypositive']
        report = self.analysis.collate_data(test_input)

        self.assertEqual(report['total'], 8)
        self.assertEqual(report['neutral'], 3)
        self.assertEqual(report['positive'], 2)
        self.assertEqual(report['verypositive'], 1)
        self.assertEqual(report['negative'], 1)
        self.assertEqual(report['verynegative'], 1)
