#!/usr/bin/env python3
"""
Initiating module
"""
from flask import Flask, render_template
from flask_babel import Babel


class Config:
    LANGUAGES = ["en", "fr"]


conf = Config()
app = Flask(__name__)
app.config['BABEL_DEFAULT_LOCALE'] = conf.LANGUAGES[0]
app.config['BABEL_DEFAULT_TIMEZONE'] = "UTC"

babel = Babel(app)


@app.route('/')
def index():
    """
    Function to display doc STring
    """
    return render_template('1-index.html')
