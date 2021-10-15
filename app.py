from flask import redirect, url_for, render_template, request, session, flash
from _database_model import *

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/<page>/', methods=['POST','GET'])
def show(page):
    return render_template(f'{page}.html')

if __name__ == '__main__':
    app.run(debug=True, port=5500) 