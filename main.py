from flask import *
import requests
import json

app = Flask(__name__)


url = "https://covid-19-tracking.p.rapidapi.com/v1/"

headers = {
	"X-RapidAPI-Key": "e04e892d93msh8f59f3d316df947p12c47cjsn8d90c3cafc8e",
	"X-RapidAPI-Host": "covid-19-tracking.p.rapidapi.com"
}

json_file = open('countries.json')
countries = json.load(json_file)
countrylist = []
for i in countries['countries']:
    countrylist.append(i['name'].lower())


@app.route('/')
def home():
    responses = []
    for country in countrylist:
        response = requests.request("GET", url+country, headers=headers)
        response = dict(response.json())
        responses.append(response)
    print(responses)
    return render_template('home.html', responses=responses)


if __name__ == '__main__':
    app.run()
