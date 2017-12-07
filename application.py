import os
import re
from flask import Flask, render_template, request, session, redirect, url_for
from vector_helpers import make_image, blur
from bitmap_helpers import process
from recognize import recognize, re_learn
from scipy import misc
import numpy as np

# Configure application
app = Flask(__name__)

# So we can use session
# Doesn't actually have to be secure
app.secret_key = "secrets"

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
  
@app.route("/read-vector", methods=["POST"])  
def read_vector():
    # Get path string from form
    path = request.form.get("draw")

    # Make into image with functions from vector_helpers
    image = make_image(path)

    # Recognize image (after blurring)
    character = recognize(blur(image))

    # Saves image and recognition in session
    # From https://stackoverflow.com/questions/27611216/how-to-pass-a-variable-between-flask-pages
    session["image"] = image.tolist()
    session["character"] = character

    return render_template("recognize.html", character=character)

@app.route("/read-file", methods=["POST"])  
def read_file():
    # Get file from form
    file = request.files["file"]

    # Use scipy function to read image into pixel array
    # As per https://docs.scipy.org/doc/scipy/reference/generated/scipy.misc.imread.html
    arr = misc.imread(file)

    # Send array through a bunch of functions in bitmap_helpers
    image = process(arr)

    # Recognize image
    character = recognize(image)

    # Saves image and recognition in session
    session["image"] = image.tolist()
    session["character"] = character

    return render_template("recognize.html", character=character)

@app.route("/learn", methods=["POST"])
def learn():
    # Determine whether the user is saying this was correct or not
    correct = True if request.form.get("yes") == "on" else False

    # Find what the label of the image should be
    should_be = request.form.get("num") if not correct else session["character"]

    if not should_be:
        return redirect(url_for("index"))

    should_be = int(should_be)

    # Validate label input
    if not(should_be in range(10)):
        return redirect(url_for("index"))

    # Send it to be relearned
    re_learn(np.array(session["image"]), should_be)

    return redirect(url_for("index"))


