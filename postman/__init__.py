from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from postman.config import *

app = Flask(__name__, static_folder='./static')

app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from postman.blogs.routes import blogs

app.register_blueprint(blogs)
