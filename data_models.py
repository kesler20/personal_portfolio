# built-in imports
import time
import os
from datetime import timedelta
import smtplib
# types imports
from typing import Optional, Tuple
from dataclasses import dataclass
# flask imports
from sqlalchemy import Column, String, Integer
from flask_sqlalchemy import BaseQuery, SQLAlchemy
from flask import Flask


ROOT_DIR = os.path.dirname(os.getcwd())
app = Flask(
    __name__,
    template_folder='templates',
    static_folder='static'
)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///keslerisoko.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'top secret!'
app.secret_key = 'password'
app.permanent_session_lifetime = timedelta(minutes=50)
db = SQLAlchemy(app)


class ErrorLogging(db.Model):

    __tablename__ = 'error_logging'
    session_id = Column(Integer, primary_key=True, nullable=False)
    timeID = Column(String(80), nullable=False,
                    default=time.ctime(), unique=True)
    name = Column(String(80), nullable=False,
                  default='default error', unique=True)


@dataclass
class ErrorLogger:

    def log_error(self, name):
        db.create_all()
        error_data = ErrorLogging(
            session_id=len(self.get_all_errors()),
            timeID=time.ctime(),
            name=name,
        )
        db.session.add(error_data)
        db.session.commit()

    def get_all_errors(self):
        db.create_all()
        return db.session.query(ErrorLogging).all()

    def get_error(self, timeID):
        db.create_all()
        found_errors = db.session.query(
            ErrorLogging).filter_by(timeID=timeID).first()
        if type(found_errors) == BaseQuery:
            return []
        elif found_errors == None:
            return []
        else:
            return found_errors


@dataclass
class GmailServer:
    """The Gmail server cna be used as a context manager of hte email service
    provided by google

    Example
    ---
    ```python
    with GmailServer(email_username,email_password) as email:
      email.send_email("hello how are you", "kisoko1@sheffield.ac.uk")
    ```
    """
    # Set the email server and credentials
    email_password: str
    email_username: str
    __server = smtplib.SMTP('smtp.gmail.com', 587)

    def set_server(self, server: smtplib.SMTP):
        self.__server = server

    @property
    def server(self) -> smtplib.SMTP:
        return self.__server

    def __enter__(self):
        # set the login and credentials
        self.server.starttls()
        self.server.login(self.email_username, self.email_password)
        return self

    def __exit__(self) -> None:
        # Close the server connection
        self.server.quit()

    def __build_mail(self, to: str, subject: Optional[str]) -> Tuple[str]:
        # Set the email headers
        headers = f'Subject: {"" if subject is None else subject}\n'
        headers += f"To: {to}\n"
        headers += "Content-Type: text/html; charset=utf-8\n"
        return to, headers

    def send_email(self, body: str, to: str, subject: Optional[str] = None) -> None:
        # Send the email
        to, headers = self.__build_mail(to, subject=subject)
        self.server.sendmail(self.email_username, to, headers + body)
