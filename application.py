import os
import re
from flask import Flask, jsonify, render_template, request
from helpers import make_image

# Configure application
app = Flask(__name__)


# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
def index():
  return render_template("index.html")
  
@app.route("/read", methods=["GET", "POST"])  
def read():
	# Our algorithm here
	path = request.form.get("input")
	image = make_image(path)
	return render_template("read.html", image=image, SIDE_LENGTH=100)
