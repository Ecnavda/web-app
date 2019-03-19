import ron
from pymongo import MongoClient
from flask import Flask, render_template, request
import os
APP_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_PATH = os.path.join(APP_PATH, "templates/")
# STATIC_PATH = os.path.join(APP_PATH, "static/")

# creating an instance of the Flask class using the special __name__ variable
website = Flask(
        __name__,
        # static_folder=STATIC_PATH,
        template_folder=TEMPLATE_PATH
        )

# Connecting to the database
mongoURI = ""
with open("connectionString.txt", "r") as file:
    mongoURI = file.readline()
client = MongoClient(mongoURI)
# The ronSwansonQuotes database is created if it doesn't exist
db = client.ronSwansonQuotes
# The quotes collection is created if it doesn't exist
collection = db.quotes

# Flask uses function decorators to trigger functions based on URL accessed
@website.route("/")
def index():
    return render_template("index.html")


@website.route("/mongo")
def mongo():
    return render_template("mongo.html")


# URL endpoints
@website.route("/quote")
def quote():
    quotes = ron.get_quote()
    # Passing the list of quotes to the template
    return render_template("quotes.html", quotes=quotes)


@website.route("/quote/<num>")
def index_multi(num):
    # quotes is a list
    quotes = ron.get_quotes(num)
    return render_template("quotes.html", quotes=quotes)


@website.route("/mongo/get_all", methods=['POST'])
def mongo_all():
    print(request)
    if 'raw' in request.form:
        results = collection.find()
    else:
        results = [x['quote'] for x in collection.find(projection={'_id': False})]
    return render_template('quotes.html', quotes=results)
