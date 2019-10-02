from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, static_folder='./static')

app.config['SECRET_KEY'] = '912094b2637c3880595f366060d5a3cc'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://iahjbxii:xdHS0nZ2AC648057xzkyXI9WMLRqqXyU@salt.db.elephantsql.com:5432/iahjbxii'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from postman.blogs.routes import blogs

app.register_blueprint(blogs)
