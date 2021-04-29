# Don't call this flask.py!
# Documentation for Flask can be found at:
# https://flask.palletsprojects.com/en/1.1.x/quickstart/

from flask import Flask, render_template, request, session, redirect, url_for, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
import os
from pathlib import Path 

app = Flask(__name__)
app.secret_key = b'a;lksjdf;jaKJLVnawrAz'


@app.route('/')
def index():
    return redirect(url_for('fortune'))

@app.route('/fortune/', methods=['GET'])
def fortune():
    content = "" 
    os.system("fortune >> fortune.txt")
    with open("fortune.txt", "r") as f:
        content = f.read()
        content = "<pre>" + content + "</pre>"
    os.system("rm -rf fortune.txt")
    return content

@app.route('/cowsay/<string:message>/', methods=['GET'])
def cowsay(message):
    content = ""
    os.system("cowsay " + message + " >> cowsay.txt")
    with open("cowsay.txt", "r") as f:
        content = f.read()
        content = "<pre>" + content + "</pre>"
    os.system("rm -rf cowsay.txt")
    return content


@app.route('/cowfortune/', methods=['GET'])
def cowfortune():
    outcontent = ""
    # cowsay stuff
    os.system("cowsay `fortune` >> cowsay.txt")
    with open("cowsay.txt", "r") as f:
        outcontent = f.read()
        outcontent = "<pre>" + outcontent + "</pre>"
    os.system("rm -rf cowsay.txt")

    return outcontent



