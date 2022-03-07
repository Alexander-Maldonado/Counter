from concurrent.futures import process
from flask import Flask, render_template, redirect, session
app = Flask(__name__)
from env import KEY
app.secret_key = KEY

@app.route("/")
def home():
    if "view" not in session:
        session["view"] = 0
    else:
        session["view"] +=1
    return render_template("index.html")

@app.route("/destroy_session")
def reset():
    session.clear()
    return redirect("/")

if __name__=="__main__":
    app.run(debug=True)