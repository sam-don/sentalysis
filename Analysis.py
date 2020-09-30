import requests
from dotenv import load_dotenv  # type: ignore
import os
from typing import List

load_dotenv()

DEEP_API_KEY = os.getenv("DEEP_API_KEY")

class Analysis():
    data: List[dict] = []

    @classmethod
    def analyse_text(cls, text: str) -> List[str]:
        print("\nSending data to Deep AI for analysis...\n")
        try:
            response = requests.post(
                "https://api.deepai.org/api/sentiment-analysis",
                data={
                    'text': text,
                },
                headers={
                    'api-key': DEEP_API_KEY
                }
            )

            sentiments = response.json()['output']
            return sentiments
        except:
            print("Sorry, looks like something went wrong!")
            return []

    @classmethod
    def collate_data(cls, sentiments: List[str]) -> dict:

        total = len(sentiments)

        neutral = sentiments.count('Neutral')
        positive = sentiments.count('Positive')
        verypositive = sentiments.count('Verypositive')
        negative = sentiments.count('Negative')
        verynegative = sentiments.count('Verynegative')

        report = {
            'total': total,
            'neutral': neutral,
            'positive': positive,
            'verypositive': verypositive,
            'negative': negative,
            'verynegative': verynegative
        }

        return report

    @classmethod
    def view_report(cls, data: dict) -> None:

        print(f'''
        Sentiment Analysis
        ------------------

        Total phrases analysed: {data['total']}

        {data['verypositive']} very positive phrases, {(data['verypositive'] / data['total'] * 100):.2f}%
        {data['positive']} positive phrases, {(data['positive'] / data['total'] * 100):.2f}%
        {data['neutral']} neutral phrases, {(data['neutral'] / data['total'] * 100):.2f}%
        {data['negative']} negative phrases, {(data['negative'] / data['total'] * 100):.2f}%
        {data['verynegative']} very negative phrases, {(data['verynegative'] / data['total'] * 100):.2f}%
        
        ''')

        input("Press Enter to continue")
