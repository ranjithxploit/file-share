from flask import Flask

app = Flask(__name__)

@app.route('/success/yes')
def success(name):
    return "welcome to %s!" %name

@app.route('/login' , methods = ['GET','POST'])
def login():
    