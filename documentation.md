Project Name: Handwriting-Recognizer
Description: The purpose of this web-app is to recognize a number from 0-9. Users can draw the number in an input box on the website or upload a image of their number. Users can also help the network learn by giving feedback on correctness of our network’s guesses.
(reorder - lazy rn)
Project Hierarchy:
Data
Contains files downloaded from MNIST handwritten digit database
Static
`script.js` contains logic for user drawn input 
`style.css` contains style information for templates
Templates
`index.html` contains the template for the site homepage
`recognize.html` contains the template for our networks guess. It also contains options for the user to help train our website by validating (or correcting) our guess. 
`read.html` is a page we created to help debug our “blurred” user image. This page is not displayed in the working, submitted version.
`appplication.py`
Flask application 
`recognize.py`
Guesses number from user input as well as retraining data-set with user input
`vector_helpers.py`
Calculates vectors from user input and formats in array. Also attempts to make user-drawn input look similar to database training set format
`bitmap_helpers.py`
Contains helper functions that format user uploaded input
`MNIST.py`
Preprocessing for MNIST data set. Once this data is formatted into array, we return the array to train.py. This file is only run once and just kept for reference.
`train.py`
Uses keras to train the model. Training has already been done and this file does not run unless user explicitly enters command. File has been kept for reference and completeness sake.
`modely.h5`
Contains model’s trained data. This file is saved on the server and continually updates as users add training.
Usage:
Create virtual environment for Python 3
Ubuntu: sudo apt-get install python3-pip python3-dev python-virtualenv
MacOS: virtualenv --system-site-packages -p python3    source ~/tensorflow/bin/activate

Install TensorFlow
Run command `pip3 install --upgrade tensorflow`
Instal Keras
Run command `pip install keras`
Unzip the project file
export the FLASK_APP environment variable to application.py (`export FLASK_APP=application.py`)
Type in “`flask run`” in terminal and follow the outputted site

No need to run the training files to run our project. These are left in the submission for reference. In case you DO want to re-run the training, simply type “`python train.py`”.



Users can either draw in the white box or upload an image to be recognized. Once uploaded, the user hits “Go” and is redirected to the following page:



This page displays our networks guess. We also give the user the option to help our network learn.
Simply type in the number that the prediction should be.

Credits: The software depends on the Keras library for Python3, which uses the Tensorflow library to create, train, and run the neural network. The training data was taken from the free MNIST database hosted here `mnist`. This project was inspired by the Detexify web app here `http://detexify.kirelabs.org/classify.html`.



