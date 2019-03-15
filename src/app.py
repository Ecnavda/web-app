from pymongo import MongoClient
import ron
from flask import Flask, render_template
import os
APP_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_PATH = os.path.join(APP_PATH, "templates/")
STATIC_PATH = os.path.join(APP_PATH, "static/")

# creating an instance of the Flask class using the special __name__ variable
website = Flask(
        __name__,
        static_folder=STATIC_PATH,
        template_folder=TEMPLATE_PATH
        )

"""
# Connecting to the database
mongoURI = ""
with open("connectionString.txt", "r") as file:
    mongoURI = file.readline()
client = MongoClient(mongoURI)
# The ronSwansonQuotes database is created if it doesn't exist
db = client.ronSwansonQuotes
"""

# Flask uses function decorators to trigger functions based on URL accessed
@website.route("/")
def index():
    return render_template("index.html")


@website.route("/quote")
def quote():
    quotes = ron.get_quote()
    return render_template("quotes.html", quotes=quotes)


@website.route("/quote/<num>")
def index_multi(num):
    # quotes is a list
    quotes = ron.get_quotes(num)
    return render_template("quotes.html", quotes=quotes)
