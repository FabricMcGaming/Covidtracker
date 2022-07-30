import requests
import json

API_KEY = "tLnJZ1kb5BRj"
PROJECT_TOKEN = "tu8tS2QaOuwJ"
RUN_TOKEN = "tUyEkiT3xuD"

response = requests.get(f'https://www.parsehub.com/api/v2/{PROJECT_TOKEN}/last_ready_run/data', params={"api_key":API_KEY})
print(response.text)
data = json.loads(response.text)
print(data)