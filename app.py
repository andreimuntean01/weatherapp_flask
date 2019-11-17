import json

import weather

from flask import Flask

import sys

import requests

from secrets import app_id

print(">>> ", sys.path)



app = Flask(__name__)


@app.route("/")
def Hello():
	return "Hello World!"

@app.route("/weather/")
def weather_route	():
	temp = json.dumps(weather.weather())
	return temp


@app.route("/weather/my-cities")
def weather_multiple_cities():
	return "Cluj: 15, New York: 10"

@app.route("/weather/my-cities/Cluj")
def weather_cluj():
	url = f"http://api.openweathermap.org/data/2.5/weather?q=Cluj-Napoca&appid={app_id}&units=metric"
	response = requests.get(url)
	weather_cluj = response.json()
	temp_cluj = weather_cluj["main"]["temp"]
	return {"Cluj-Napoca": temp_cluj}