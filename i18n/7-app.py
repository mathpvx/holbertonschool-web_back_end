#!/usr/bin/env python3
"""Flask app with locale and timezone selector"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, _
from typing import Optional, Dict
import pytz
from pytz.exceptions import UnknownTimeZoneError


class Config:
    """Configuration for Babel"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Optional[Dict]:
    """Mocked user login via 'login_as' URL param"""
    try:
        user_id = int(request.args.get("login_as"))
        return users.get(user_id)
    except (TypeError, ValueError):
        return None


@app.before_request
def before_request():
    """Set user in global context before each request"""
    g.user = get_user()


@babel.localeselector_function
def get_locale():
    """Determine the best match for supported languages"""
    # URL param has priority
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale

    # User preference
    user = g.get('user')
    if user:
        user_locale = user.get("locale")
        if user_locale in app.config['LANGUAGES']:
            return user_locale

    # Fallback to header
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone():
    """Select the appropriate timezone"""
    # 1. Check URL
    tz_param = request.args.get('timezone')
    if tz_param:
        try:
            return pytz.timezone(tz_param).zone
        except UnknownTimeZoneError:
            pass

    # 2. Check user
    user = g.get('user')
    if user:
        tz = user.get("timezone")
        try:
            return pytz.timezone(tz).zone
        except (UnknownTimeZoneError, TypeError):
            pass

    # 3. Default
    return app.config['BABEL_DEFAULT_TIMEZONE']


@app.route('/')
def index():
    """Main page"""
    return render_template('7-index.html')


if __name__ == '__main__':
    app.run()
