import requests

url = "http://127.0.0.1:8000/predict"
data = {"text": "Win a free iPhone now! Click here."}

response = requests.post(url, json=data)

print("Response:", response.json())  # Expected: Scam or Not Scam
