from flask import Flask, render_template,redirect, url_for,request,session
import os
import random, string

app = Flask(__name__)
app.secret_key = os.urandom(100)
user = {
    "email":"admin@email.com",
    "password":"admin123",
    "token":''
}

msg = None

def createToken(length):
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for i in range(length))

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

@app.route('/logout')
def dropsession():
    session.pop('user', None)
    print('logging out app')
    return render_template('login.html')

@app.route('/login',methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        result = request.form

        if result.get('email') == user.get('email') and result.get('password')==user.get('password'):
            session['user'] = None
            session['user'] = result.get('email')
            user['token'] = createToken(20)
            #return redirect(url_for('updatemail'))
            return render_template('updateemail.html',csrf=user.get('token'))
    return index()

if __name__ == "__main__":
    app.run(debug=True)