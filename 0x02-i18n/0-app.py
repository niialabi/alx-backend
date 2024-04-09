#!/usr/bin/env python3
""" flask defalt app """
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """ renders default index page via template """
    return render_template('0-index.html')
