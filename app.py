#  import libaries
from flask import Flask, render_template

# import os
# import json
# import requests

# Flask Setup
app = Flask(__name__)


# create a route that renders the index.html template
@app.route("/")
def home():
    return render_template("index.html")

# create a route that renders the beerdata.html template
@app.route("/beerdata")
def beerdata():
    return render_template("beerdata.html")

# create a route that renders the brewingplots.html template
@app.route("/brewingplots")
def brewingplots():
    return render_template("brewingplots.html")

# create a route that renders the gallery.html template
@app.route("/gallery")
def gallery():
    return render_template("gallery.html")

# create a route that renders the mapping.html template
@app.route("/mapping")
def mapping():
    return render_template("mapping.html")

# create a route that renders the top_ABV.html template
@app.route("/top_ABV")
def top_ABV():
    return render_template("top_ABV.html")

if __name__ == "__main__":
    app.run()