import requests
from dotenv import load_dotenv  # type: ignore
import os
from typing import List

load_dotenv()

DEEP_API_KEY = os.getenv("DEEP_API_KEY")

class Analysis():
    data: List[dict] = []

    @classmethod
    def analyse_text(cls, text):
        r = requests.post(
            "https://api.deepai.org/api/sentiment-analysis",
            data={
                'text': text,
            },
            headers={
                'api-key': DEEP_API_KEY
            }
        )

        sentiments = r.json()['output']

        total = len(sentiments)

        neutral = sentiments.count('Neutral')
        positive = sentiments.count('Positive')
        negative = sentiments.count('Negative')

        print(f'''
        Sentiment Analysis
        ------------------

        Total phrases analysed: {total}

        {positive} positive phrases, {(positive / total * 100):.2f}%
        {neutral} neutral phrases, {(neutral / total * 100):.2f}%
        {negative} negative phrases, {(negative / total * 100):.2f}%


        ''')
