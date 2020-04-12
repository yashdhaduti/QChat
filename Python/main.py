import pyrebase
import doordashbot as dd

from flask import *

config = {
    "apiKey": "AIzaSyDnTOuGzFCMsoNqMg-I_keSS74QIPjnjHw",
    "authDomain": "qchat-d4942.firebaseapp.com",
    "databaseURL": "https://qchat-d4942.firebaseio.com",
    "projectId": "qchat-d4942",
    "storageBucket": "qchat-d4942.appspot.com",
    "messagingSenderId": "95527175582",
    "appId": "1:95527175582:web:4de2e129b5a52c1ee5028f",
    "measurementId": "G-90D5J59X9V"
  }

firebase = pyrebase.initialize_app(config)
db = firebase.database()
app = Flask(__name__)
app.config['SESSION_COOKIE_SECURE'] = False

@app.route("/login", methods=["POST", "GET"])
def login():
    inDict=False
    if request.method == 'POST':
        user = request.form['name']
        if user == "":
            return render_template("login.html")
        else:      
            for i in db.child("names").get().val().values():
                if i == user:
                    inDict=True
                    break
            if inDict==False:
                db.child("names").push(user)
            return redirect(url_for("default",usr=user))
    else:
        return render_template("login.html")

@app.route("/<usr>", methods=['POST', 'GET'])
def default(usr):
    inDict=False
    for i in db.child("names").get().val().values():
        if i == usr:
            inDict=True
            break

    if inDict==False:
        return render_template('login.html')
    else:
        return render_template('base.html', title=usr)


@app.route("/swipe", methods=['POST', 'GET'])
def swipe():
    if request.method == 'POST':
        temp = request.form["phone"]
        db.child("names").child("info").push(temp)
        temp = request.form["gender"]
        db.child("names").child("info").push(temp)
        temp = request.form["pref"]
        db.child("names").child("info").push(temp)
        temp = request.form["address"]
        db.child("names").child("info").push(temp)
        temp = request.form["cc"]
        db.child("names").child("info").push(temp)
        return redirect("https://normanwang1234.github.io/swipe/")
    else:
        return redirect(url_for("login"))

@app.route("/order/", methods=['POST', 'GET'])
def order():
    if request.method == 'POST':
        temp = request.form["resOrder"]
        db.child("names").child("orders").push(temp)
        temp = request.form["menOrder"]
        db.child("names").child("orders").push(temp)
        return redirect("https://normanwang1234.github.io/call")
    else:
        return render_template("orders.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
