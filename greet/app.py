from flask import Flask
import unittest
app = Flask(__name__)
app.debug = True

@app.route("/welcome")
def welcome():
    return 'Welcome'

@app.route("/welcome/home")
def welcome_home():
    return "Welcome Home"
@app.route("/welcome/back")
def welcome_back():
    return "Welcome back"
