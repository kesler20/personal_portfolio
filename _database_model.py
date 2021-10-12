from datetime import timedelta
from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy

ROOT_DIR = os.path.dirname(os.getcwd())
app = Flask(
    __name__, 
    template_folder='templates',
    static_folder='static'
)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///isokoin.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'top secret!'
app.secret_key = 'password'
app.permanent_session_lifetime = timedelta(minutes=50)
db = SQLAlchemy(app)
