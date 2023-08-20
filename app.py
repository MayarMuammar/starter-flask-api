from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, world! \n This is Backend for NLP Service of the Family Doctor Project'