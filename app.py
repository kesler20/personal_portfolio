from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
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

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/<page>/', methods=['POST','GET'])
def show(page):
    return render_template(f'{page}.html')

if __name__ == '__main__':
    app.run(debug=True, port=5500) 