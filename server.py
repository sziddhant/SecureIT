from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os
from sqlalchemy.orm import sessionmaker
from tabledef import *
from input import *
engine = create_engine('sqlite:///credential.db', echo=True)
from otp import *

app = Flask(__name__)



@app.route('/camera')
def cam():
    return redirect("http://192.168.2.104:8081", code=302)

@app.route('/a')
def welcome():
    return "Welcome to SecureIT's unsecure backend"


@app.route('/otp')
def run():
    x = generate_otp()
    pass_verify(x)
    return str(x)


@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')

    else:
        return 'Hello ! <br> <a href=" / logout">Logout</a><br> <a href=" /otp">Generate OTP</a> <br> <a href=" /camera">Camera</a>'


@app.route('/login', methods=['POST'])
def do_admin_login():


    POST_USERNAME = str(request.form['username'])
    POST_PASSWORD = str(request.form['password'])

    Session = sessionmaker(bind=engine)
    s =    Session()
    query = s.query(User).filter(User.username.in_([POST_USERNAME]), User.password.in_([POST_PASSWORD]))
    result = query.first()
    if result:

        session['logged_in'] = True
        login_log_file = open('login_log.txt', 'a+')
        login_log_file.write('%s  \n'%POST_USERNAME)
        login_log_file.close()
    else:
        flash('wrong password!')
    return home()


@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()



if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(host='0.0.0.0', port=5000)