from flask import *
import requests
import json

app = Flask(__name__)

url = "https://covid-19-tracking.p.rapidapi.com/v1/usa"

headers = {
	"X-RapidAPI-Key": "e04e892d93msh8f59f3d316df947p12c47cjsn8d90c3cafc8e",
	"X-RapidAPI-Host": "covid-19-tracking.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)
response = dict(response.json())
print(response)


@app.route('/')
def home():
    response = requests.request("GET", url, headers=headers)
    response = dict(response.json())
    print(response.__dict__)
    return render_template('home.html', response=response)


if __name__ == '__main__':
    app.run()
