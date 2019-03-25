from flask import Flask
from flask import  render_template, jsonify, request
import requests
app = Flask(__name__)


@app.route('/')
def hello_world():
    """
    Sample hello world
    """

    return render_template('home.html')

