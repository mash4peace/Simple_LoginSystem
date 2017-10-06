from flask import Flask, session, render_template, request, redirect, g, url_for
import os
from  flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired

print("Everything is OK")

app = Flask(__name__)
app.secret_key = os.urandom(5)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        session.pop('user', None)

        if request.form['password'] == '12345':
            session['user'] = request.form['username']
            return redirect(url_for('protected'))

    return render_template('index.html')

@app.route('/protected', methods= ["GET","POST"])
def protected():
    if g.user:
        return render_template('protected.html')

    return redirect(url_for('index'))

@app.before_request
def before_request():
    g.user = None
    if 'user' in session:
        g.user = session['user']

@app.route('/getsession')
def getsession():
    if 'user' in session:
        return session['user']

    return 'Not logged in!'

@app.route('/dropsession')
def dropsession():
    session.pop('user', None)
    return 'Dropped!'

if __name__ == '__main__':
    app.run(debug=True)
