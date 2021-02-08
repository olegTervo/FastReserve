from flask import Flask
from flask import redirect, render_template, request, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash
from os import getenv
from os import urandom

app = Flask(__name__)
app.secret_key = urandom(16).hex() #getenv("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
db = SQLAlchemy(app)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/orders")
def ordersPage():
	offers = ["vasara","polkkupyörä","CS peli",getenv("SECRET_KEY"),urandom(16).hex()]
	return render_template("orders.html", message="Tässä on kaikki tarjoukset", items=offers)

@app.route("/orders/<int:id>")
def orderPage(id):
	return "Order #" + str(id)

@app.route("/login",methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    hash_value = generate_password_hash(password)
    sql = "SELECT password FROM Users WHERE email=:username"
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()    
    if user == None:
       redirect("/")
    else:
        hash_value = user[0]
        if check_password_hash(hash_value,password):
            session["username"] = username
        else:
            redirect("/")
    
    return redirect("/")

@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/")

@app.route("/signin", methods=["GET"])
def signin():
    return render_template("signIn.html")

@app.route("/signin", methods=["POST"])
def signinpost():
    name = request.form["name"]
    secondname = request.form["secondname"]
    email = request.form["email"]
    phone = request.form["phone"]
    password = request.form["password"]
    if(request.form.get("isModerator")): 
        isModerator = '1'
    else:
        isModerator = '0'

    hash_value = generate_password_hash(password)
    sql = "INSERT INTO Users (name,secondname,email,phonenumber,password,ismoderator) VALUES (:name,:secondname,:email,:phone,:password,:isModerator)"
    db.session.execute(sql, {"name":name,"secondname":secondname,"email":email,"phone":phone, "password":hash_value, "isModerator":isModerator})
    db.session.commit()

    return redirect("/")
