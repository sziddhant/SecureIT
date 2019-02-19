from flask import Flask
from otp import *
app = Flask(__name__)

print (generate_otp())
@app.route('/otp')
def run():
    x= generate_otp()
    return x
