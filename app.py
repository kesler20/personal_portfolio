from flask import redirect, url_for, render_template, request, session, flash
from _database_model import *

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/<page>/', methods=['POST','GET'])
def show(page):
    return render_template(f'{page}.html')

@app.route('/thankyou', methods=['POST','GET'])
def contact_me():
    if request.method == 'POST':
        service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
        emailMsg = request.form['msg']
        mimeMessage = MIMEMultipart()
        mimeMessage['to'] = request.form['email']
        try:
            mimeMessage['subject'] = request.form['subject']
        except:
            mimeMessage['subject'] = f"{request.form['name']}, {request.form['company']}"
        mimeMessage.attach(MIMEText(emailMsg, 'plain'))
        raw_string = base64.urlsafe_b64encode(mimeMessage.as_bytes()).decode()

        message = service.users().messages().send(userId='me', body={'raw': raw_string}).execute()
        print(message)
        return render_template('thankyou.html', user=request.form['email'])
    else:
        return render_template('thankyou.html', user='None')

if __name__ == '__main__':
    app.run(debug=True, port=5500) 