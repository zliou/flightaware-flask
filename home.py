from flask import Flask, render_template
import requests


API_KEY = "temp"
API_URL = "https://aeroapi.flightaware.com/aeroapi/"


app = Flask(__name__)

def make_request():
    flight_iata = "AS3457"
    auth_header = {'x-apikey': API_KEY}

    response = requests.get(API_URL + f"flights/{flight_iata}", headers=auth_header)

    if response.status_code == 200:
        response = response.json()
        for k in response["flights"]:
            print(k, ":" )
            print("------")
        
    else:
        print("error")
    

@app.route('/')
@app.route('/home')
def home():
    make_request()
    return "<p>Hello there.</p>"


