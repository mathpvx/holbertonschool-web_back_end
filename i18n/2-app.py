#!/usr/bin/env python3
"""
Basic Flask App

This module creates a simple Flask web application
with one route that renders a basic HTML template.
"""

from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """
    Config class for Flask app and Babel.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)

def get_locale():
    """
    Select the best matching language based on the request.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


babel = Babel()
babel.init_app(app, locale_selector=get_locale)


@app.route('/')
def hello():
    """
    Route handler for the root URL.

    Returns:
        str: Rendered HTML content from the template.
    """
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run()
