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


# Important functions and vars
def updateViews():
    views = db.execute("SELECT * FROM views")
    views = views[0]['Views']
    views += 1
    print(views)
    db.execute("UPDATE views set Views=:views", views=views)

hardwareTopicsList = ["Introduction", "CPU", "RAM", "Storage", "GPU", "Motherboard", "Power Supply", "Monitor", "Other Peripherals"]
hardwareLinks = ["/hardware_intro", "/cpu", "/ram", "/storage", "/gpu", "/mb", "/psu", "/monitor", "/periphs"]

# ROUTES 

@app.route("/", methods=["GET"])
def home():
    updateViews()
    return render_template("home.html")

@app.route("/register", methods=["GET", "POST"])
def signUp():
    updateViews()
    if request.method == "GET":
        return render_template("register.html", usernameErr=None, emailErr=None)
    else:
        print("Post request made")
        theForm = request.form
        email = theForm.get("email")
        username = theForm.get("username")
        pwHash = generate_password_hash(theForm.get("password"))
        print(email)
        print(username)
        print(pwHash)

        if len(db.execute("SELECT * FROM users WHERE username = :username", username=username)) != 0:
            return render_template("register.html", usenameErr="This username is already taken!", emailErr=None)
        elif len(db.execute("SELECT * FROM users WHERE email = :email", email=email)) != 0:
            return render_template("register.html", emailErr="This email has already been used!", usernameErr=None)

        db.execute("INSERT INTO users (email, username, pw_hash) VALUES (:email, :username, :pw_hash)", email=email, username = username, pw_hash = pwHash)
        return redirect("/")

@app.route("/login", methods=["GET", "POST"])
def login():
    updateViews()

    if request.method == "GET":
        return render_template("login.html")

    else:
        print("POST REQUEST MADE")
        username = request.form.get("email")
        pw = request.form.get("password")

        check = db.execute("SELECT * FROM users WHERE username=:username", username = username)
        
        if len(check) != 1 or not check_password_hash(check[0]["pw_hash"], pw):
            return render_template("login.html", invalid=True)
        
        session["user_id"] = check[0]["id"]
        
        return redirect("/")

@app.route('/home', methods=["GET", "POST"])
def homeLoggedIn():
    updateViews()
    return render_template("homeLoggedIn.html", hardwareTopicsList = hardwareTopicsList, hardwareLinks = hardwareLinks)