import smtplib
from config import email_username, email_password
import yagmail
import smtplib
from flask import redirect, url_for, render_template, request
from data_models import app, ErrorLogger


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/<page>/', methods=['POST', 'GET'])
def show(page):

    if page == "errors":
        error_logger = ErrorLogger()
        errors = error_logger.get_all_errors()
        response = [{"name": error_logging.name, "time": error_logging.timeID}
                    for error_logging in errors]
        return { "errors" : response }

    if page == 'thankyou':
        # this is the form of request expected
        # ImmutableMultiDict([
        #     ('name', 'kesler isoko'),
        #     ('company', 'student'),
        #     ('msg', 'ththththt'),
        #     ('email', 'kisoko1@sheffield.ac.uk')
        # ])
        # the Immutable dict object can be accessed from the request.form
        # as such "request.form['name']" -> 'kesler isoko'

        # if the user posts to the thank you route
        # sen the form data via email
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
            except smtplib.SMTPAuthenticationError as error:
                error_logger = ErrorLogger()
                error_logger.log_error(error.smtp_error.decode())
        else:
            # if the get request is called as the user refreshes the page
            # redirect the user to the home page
            return redirect(url_for("/index"))

    return render_template(f'{page}.html')


@app.route('/errors/<name>/')
def show_errors_logged(name):
    error_logger = ErrorLogger()
    error_logging = error_logger.get_error(name)
    return {"name": error_logging.name, "time": error_logging.timeID}


if __name__ == '__main__':
    app.run(debug=True, port=5500)
