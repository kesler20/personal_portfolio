import smtplib
import yagmail
from config import email_username, email_password
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
    if page == "thankyou":
        """
        this is the form of request expected
        
        ```txt
        ImmutableMultiDict([
        ('name', 'kesler isoko'), 
        ('company', 'student'), 
        ('msg', 'ththththt'), 
        ('email', 'kisoko1@sheffield.ac.uk')
        ])
        ```
        the Immutable dict object can be accessed from the request.form
        as such ``request.form['name']`` -> ``'kesler isoko'``
        """
        if request.method == "POST":
            # Set the login credentials and email server
            yag = yagmail.SMTP(email_username, email_password)
            try:
                yag.login()

                # Set the recipient and email content
                to = request.form['email']
                subject = f"Message by {request.form['name']} from {request.form['company']}"
                body = request.form['msg']

                # Send the email
                yag.send(to, subject, body)
            except smtplib.SMTPAuthenticationError:
                pass
            
    return render_template(f'{page}.html')
if __name__ == '__main__':
    app.run(debug=True, port=5500) 