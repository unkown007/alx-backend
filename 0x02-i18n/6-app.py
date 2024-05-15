#!/usr/bin/env python3
""" Python Flask app
"""
from flask import Flask, request, render_template, g
from flask_babel import Babel, force_locale


class Config(object):
    """ Set up and define app configurations
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}
app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """ Return a best locale match """
    locale = request.args.get('locale', '')
    if locale in app.config["LANGUAGES"]:
        return locale
    if g.user and g.user['locale'] in app.config["LANGUAGES"]:
        return g.user['locale']
    header_locale = request.headers.get('locale', '')
    if header_locale in app.config["LANGUAGES"]:
        return header_locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user():
    """ Get a user on the database """
    login_as = request.args.get("login_as")
    if login_as and users.get(int(login_as)):
        return users.get(int(login_as))
    return None


@app.before_request
def before_request():
    """ Get a user befor any function/method is executed """
    g.user = get_user()


@app.route('/', strict_slashes=False)
def hello():
    """ Render a template
    """
    if g.user is not None:
        return render_template('6-index.html', user=g.user.get("name", ""))
    return render_template('6-index.html')


if __name__ == "__main__":
    """ Main Function """
    app.run(host="0.0.0.0", port=5000)
