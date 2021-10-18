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

API_kEYS = 'AIzaSyCOtUVXjkThgCrsmJUTBN0JoTfUDRF-7uw'
from taskapi import Create_Service
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

CLIENT_SECRET_FILE = 'client_secret_971955567226-7b8bhee7fa4krl3qqetea54d0ojdjblt.apps.googleusercontent.com.json'
API_NAME = 'gmail'
API_VERSION = 'v1'
SCOPES = ['https://mail.google.com/']

