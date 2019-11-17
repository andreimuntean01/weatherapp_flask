import json

import weather

from flask import Flask

import sys

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