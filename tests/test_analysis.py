import unittest
import Analysis
from Analysis import Analysis

class TestAnalysisMethods(unittest.TestCase):

    def test_analyse_text(self):
        """Test if retrieving specific user tweets returns list correctly.
        This test will return an empty list and should still pass if 
        there is no Twitter Bearer Token available.
        """
        analysis = Analysis()
        test_input = "This is some text to analyse.\
             If a Deep AI API Key is not available to use it will return an empty list."
        result = analysis.analyse_text(test_input)
        self.assertIsInstance(result, list)
