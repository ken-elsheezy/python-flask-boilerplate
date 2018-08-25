import os
from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension
from .database_config import database
from .login_config import login_manager
from website import hyperlinks


basedir = os.path.abspath(os.path.dirname(__file__))
APP_ROOT = os.path.dirname(os.path.abspath(__file__))


application = app = Flask(__name__)
app.config['SECRET_KEY'] = 'generate-a random-key-and-paste-here'
app.config['DEBUG'] = True

#Ensure you register your blueprints as below.
#Feel free to create your own blueprint, check website/__init__.py for an example
app.register_blueprint(hyperlinks)
