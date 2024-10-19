from flask import *
import requests
import json

app=Flask(__name__)

API_KEY="04cda2461dmshb8a078a6f91bc46p167ef6jsnecfc65eeff9b"

@app.route("/")
def home():
    return redirect(url_for("trending"))

@app.route("/trending")
def trending():
    url = "https://indian-stock-exchange-api2.p.rapidapi.com/trending"

    headers = {
        "x-rapidapi-key": API_KEY ,
        "x-rapidapi-host": "indian-stock-exchange-api2.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)

    return render_template('trending.html', context=response.json())

@app.route("/historicaldata")
def historicaldata():
    return render_template("base.html")

@app.route("/historicaldata", methods=['POST'])
def historical_data():
    stockname=request.form["text"]
    url = "https://indian-stock-exchange-api2.p.rapidapi.com/historical_data"

    querystring = {"stock_name":stockname,"period":"1m","filter":"price"}

    headers = {
        "x-rapidapi-key": API_KEY,
        "x-rapidapi-host": "indian-stock-exchange-api2.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    return response.json()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)