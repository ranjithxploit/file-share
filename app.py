from flask import Flask, redirect, url_for, request

app = Flask(__name__)

@app.route('/success/yes')
def success(name):
    return "welcome to %s!" %name

@app.route('/login' , methods = ['GET','POST'])
def login():
    if request.method=='POST':
        user=request.form["ab"]
        return redirect(url_for("success", name=user))
    else:
        user=request.args.get('ab')
        return redirect(url_for('success', name=user))

if __name__ =='main':
    app.run(debug=True)        