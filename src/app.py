import ron
import json
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
@website.route("/get_quote")
def quote():
    quote = ron.get_quote()
    return json.dumps(quote)


@website.route("/get_quote/<num>")
def quotes(num):
    quotes = ron.get_quotes(num)
    return json.dumps(quotes)


@website.route("/get_mongo", methods=['POST'])
def mongo_get():
    if 'raw' in request.form:
        results = [doc for doc in collection.find()]
    else:
        results = [doc['quote'] for doc in collection.find(projection={'_id': False})]
    return json.dumps(results)

# Deprecated ---------------------------------------------------
@website.route("/quote_html")
def quote_html():
    quotes = ron.get_quote()
    # Passing the list of quotes to the template
    return render_template("quotes.html", quotes=quotes)


@website.route("/quote_html/<num>")
def quote_multi_html(num):
    # quotes is a list
    quotes = ron.get_quotes(num)
    return render_template("quotes.html", quotes=quotes)


@website.route("/get_mongo_html", methods=['POST'])
def mongo_all_html():
    if 'raw' in request.form:
        results = collection.find()
    else:
        results = [x['quote'] for x in collection.find(projection={'_id': False})]
    return render_template('quotes.html', quotes=results)
