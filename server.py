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

msg = None

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/update',methods=['GET', 'POST'])
def updatemail():
    if 'user' in session:
        if request.method == 'POST':
                result = request.form
                print(result)
                print(user)
                if result.get('csrf') == user.get('token'):
                    user['email'] = result.get('email')
                    user['password'] = result.get('password')
                    msg = 'sucess'
                    print('tokens are valid')
                else:
                    msg = 'fail'
                    print('tokens not valid')
        return render_template('updateemail.html',msg=msg)
    return redirect(url_for('login'))


@app.route('/login',methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        result = request.form
        
        if result.get('email') == user.get('email') and result.get('password')==user.get('password'):
            session['user'] = result.get('email')
            user['token'] = 'myappserert'
            #return redirect(url_for('updatemail'))
            return render_template('updateemail.html',csrf=user.get('token'))
    return index()

if __name__ == "__main__":
    app.run(debug=True)