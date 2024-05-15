#!/usr/bin/env python3
""" Python Flask app
"""
from flask import Flask, request, render_template
from flask_babel import Babel


class Config(object):
    """ Set up and define app configurations
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """ Return a best locale match """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def hello():
    """ Render a template
    """
    return render_template('2-index.html')


if __name__ == "__main__":
    """ Main Function """
    app.run(host="0.0.0.0", port=5000)
