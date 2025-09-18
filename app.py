from flask import Flask, redirect, url_for, request

app = Flask(__name__)

@app.route('/success/index')
def success(name):
    return "welcome to %s!" %name

@app.route('/login' , methods = ['GET','POST'])
def login():
    if request.method=='POST':
        user=request.form["abcd"]
        return redirect(url_for("success", name=user))
    else:
        user=request.args.get('abcd')
        return redirect(url_for('success', name=user))

if __name__ =='__main__':
    app.run(debug=True)