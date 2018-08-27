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

# DATABASE CONNECTION
# 1. If you want to use a local Database (it would save to the configuration folder), uncomment below line 
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'your_database_name.db')

# 2. If you want to use a remote MySQL Database like AWS RDS, uncomment below line
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://<db_user>:<db_password>@<endpoint>/<db_url>'



#Ensure you register your blueprints as below.
#Feel free to create your own blueprint, check website/__init__.py for an example
app.register_blueprint(hyperlinks)
