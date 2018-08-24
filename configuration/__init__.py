import os
from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension


basedir = os.path.abspath(os.path.dirname(__file__))
APP_ROOT = os.path.dirname(os.path.abspath(__file__))


application = app = Flask(__name__)
app.config['SECRET_KEY'] = 'generate-a random-key-and-paste-here'
app.config['DEBUG'] = True
