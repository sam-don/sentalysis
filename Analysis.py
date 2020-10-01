import requests
from dotenv import load_dotenv  # type: ignore
import os
import json
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
        except Exception:
            print("\nSorry, looks like something went wrong!")
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
    def view_report(cls, data: dict, saved: bool = False) -> None:

        print(f'''
        Sentiment Analysis
        ------------------

        Total phrases analysed: {data['total']}

        {data['positive']} positive phrases,\
 {(data['positive'] / data['total'] * 100):.2f}%
        {data['verypositive']} very positive phrases,\
 {(data['verypositive'] / data['total'] * 100):.2f}%
        {data['neutral']} neutral phrases,\
 {(data['neutral'] / data['total'] * 100):.2f}%
        {data['negative']} negative phrases,\
 {(data['negative'] / data['total'] * 100):.2f}%
        {data['verynegative']} very negative phrases,\
 {(data['verynegative'] / data['total'] * 100):.2f}%

        ''')

        if not saved:
            user_option = input("Would you like to save this report? (y/n) ")

            if user_option == 'y':
                cls.save_file(data)
        else:
            user_option = input("Press Enter to return to main menu.")

    @classmethod
    def read_file(cls, file):
        try:
            with open(file) as f:
                data = f.read()

                return data
        except Exception:
            print("\nThere was an error opening this file.")
            return ''

    @classmethod
    def save_file(cls, report):
        name = input("\nWhat would you like to name this report?")

        saved = {
            'name': name,
            'report': report
        }

        cls.data.append(saved)

        with open("saved_reports.json", "w") as outfile:
            json.dump(cls.data, outfile)

        print("\nReport saved to file.")

        return saved

    @classmethod
    def load_saved(cls):
        try:
            json_data = cls.read_file('saved_reports.json')
            cls.data = json.loads(json_data)
        except Exception:
            saved_reports = []
            with open("saved_reports.json", "w") as f:
                json_data = json.dumps(saved_reports)
                f.write(json_data)

    @classmethod
    def view_saved(cls):
        print("")
        for index, report in enumerate(cls.data):
            print(f"{index+1}. {report['name']}")

        selection = input("\nWhich report would you like to see? ")

        cls.view_report(cls.data[int(selection)-1]['report'], True)
