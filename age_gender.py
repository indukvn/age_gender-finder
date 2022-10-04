import datetime
from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def blog():
    return "<h1>Hello there!</h1>" \
           "<h2>Tap 'guess/your_name'</h2>"


@app.route('/guess/<name>')
def data(name):
    current_date = datetime.datetime.now()
    current_year = current_date.strftime("%Y")

    gender_api = f"https://api.genderize.io?name={name}"
    gender_response = requests.get(gender_api).json()
    gender = gender_response["gender"]

    age_api = f"https://api.agify.io?name={name}"
    age_response = requests.get(age_api).json()
    age = age_response["age"]
    return render_template("index.html", gender=gender, age=age, name=name, CURRENT_YEAR=current_year)


if __name__ == "__main__":
    app.run(debug=True)