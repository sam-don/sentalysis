import requests

r = requests.post(
    "https://api.deepai.org/api/sentiment-analysis",
    data={
        'text': 'This is awesome!',
    },
    headers={'api-key': '644f22d1-b49f-44ab-aca2-f849fdf7d411'}
)
print(r.json())