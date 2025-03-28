#!/usr/bin/env python3
""" Flask app with template translations using Babel."""

from flask import Flask, render_template, request
from flask_babel import Babel, _


class Config:
    """ Configuration class for Babel and Flask."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)


def get_locale():
    """ Determines the best match for supported languages."""
    return request.accept_languages.best_match(app.config["LANGUAGES"])


babel = Babel(app, locale_selector=get_locale)


@app.route('/')
def index():
    """ Renders the index page."""
    return render_template("3-index.html")


if __name__ == '__main__':
    app.run()
