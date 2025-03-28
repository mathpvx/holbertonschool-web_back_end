#!/usr/bin/env python3
"""Flask app with user login mock and localization"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, _
from typing import Optional, Dict


class Config:
    """App configuration"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


# Mock user database
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_locale() -> str:
    """Determine best-matching locale"""
    locale = request.args.get('locale')
    if locale in Config.LANGUAGES:
        return locale
    return request.accept_languages.best_match(Config.LANGUAGES)


def get_user() -> Optional[Dict]:
    """Retrieve user from mock db via login_as param"""
    try:
        user_id = int(request.args.get('login_as'))
        return users.get(user_id)
    except (TypeError, ValueError):
        return None


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel()
babel.init_app(app, locale_selector=get_locale)


@app.before_request
def before_request():
    """Run before each request to set user context"""
    g.user = get_user()


@app.route('/')
def index():
    """Render index page"""
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run()
