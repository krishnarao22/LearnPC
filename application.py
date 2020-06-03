import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

# Lines 14 - 38 credit CS50

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///learnPC.db")

def updateViews():
    views = db.execute("SELECT * FROM views")
    views = views[0]['Views']
    views += 1
    print(views)
    db.execute("UPDATE views set Views=:views", views=views)

@app.route("/", methods=["GET"])
def home():
    updateViews()
    return render_template("home.html")

@app.route("/sign_up", methods=["GET"])
def renderSignUp():
    updateViews()
    if request.method == "GET":
        return render_template("login.html")

"""
@app.route("/sign_up", methods=["POST"])
def signUp():
    email = request.form.get("email")
    usernames = db.execute("SELECT username FROM users")
    print(usernames)
    return("ok")
"""