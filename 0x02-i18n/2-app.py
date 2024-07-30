#!/usr/bin/env python3
"""
Flask app initialization module
"""

from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """
    Configure environs.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)


@babel.localeselector
def get_locale():
    # Use the app configuration directly
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """
    Renders the home page.
    """
    return render_template('2-index.html')
