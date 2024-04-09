#!/usr/bin/env python3
""" flask defalt app """
from flask import Flask, render_template
from flask_babel import Babel, request

app = Flask(__name__)
babel = Babel(app)


class Config:
    """ Config class """

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def world():
    """ renders default 2- index page via template """
    return render_template('1-index.html')


@babel.localeselector
def get_locale():
    """ get local """
    return request.accept_languages.best_match(app.config['LANGUAGES'])
