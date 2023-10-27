from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY'] = '7c342e9dfb6921e7c835f4b2'
db = SQLAlchemy(app)

##contexto
app.app_context().push()

from market import routes

