from flask import Flask, render_template,redirect, url_for,request,session
from flask_wtf import FlaskForm
from wtforms import StringField
from flask_login import LoginManager, login_required, login_user, logout_user, UserMixin, current_user
import os

app = Flask(__name__)
app.secret_key = os.urandom(100)
user = {
    "email":"admin@email.com",
    "password":"admin123",
    "token":''
}


@app.route('/')
def index():
    return render_template('login.html')

@app.route('/update',methods=['GET', 'POST'])
def updatemail():
    if request.method == 'POST':
             result = request.form
             print(result)
             user['email'] = result.get('email')
             user['password'] = result.get('password')
    return render_template('updateemail.html')


@app.route('/login',methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        result = request.form
        
        if result.get('email') == user.get('email') and result.get('password')==user.get('password'):
            session['username'] = result.get('email')
            return redirect(url_for('updatemail'))
    return index()

if __name__ == "__main__":
    app.run(debug=True)