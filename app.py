from flask import Flask
app = Flask(__name__)

#create templates index.html reading code


@app.route('/')
def hello_world():
    return "hello"

@app.route('/admin')
def admin_panel():
    return "this is admin panel"

@app.route('/login')
def login():
    return "Login page"

if  __name__== '__main__':
    app.run()