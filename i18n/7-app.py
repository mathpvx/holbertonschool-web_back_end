#!/usr/bin/env python3
"""Flask app with Babel i18n and timezone support"""

from flask import Flask, render_template, request, g
from flask_babel import Babel
from pytz import timezone, UnknownTimeZoneError

app = Flask(__name__)


class Config:
    """App configuration class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """Get user dictionary from mock DB based on login_as query param"""
    try:
        user_id = int(request.args.get("login_as"))
        return users.get(user_id)
    except (TypeError, ValueError):
        return None


@app.before_request
def before_request():
    """Set user as global before handling request"""
    g.user = get_user()
    g.locale = get_locale()


def get_locale():
    """Select the best match for supported languages"""
    query_locale = request.args.get("locale")
    if query_locale in app.config["LANGUAGES"]:
        return query_locale

    if g.get("user"):
        user_locale = g.user.get("locale")
        if user_locale in app.config["LANGUAGES"]:
            return user_locale

    return request.accept_languages.best_match(app.config["LANGUAGES"])


def get_timezone():
    """Select the most appropriate timezone"""
    try:
        query_tz = request.args.get("timezone")
        if query_tz:
            return timezone(query_tz).zone
        if g.get("user"):
            return timezone(g.user["timezone"]).zone
    except UnknownTimeZoneError:
        return app.config["BABEL_DEFAULT_TIMEZONE"]
    return app.config["BABEL_DEFAULT_TIMEZONE"]


babel = Babel(app, locale_selector=get_locale, timezone_selector=get_timezone)


@app.route('/')
def index():
    """Render main index page"""
    return render_template("7-index.html")


if __name__ == '__main__':
    app.run()
