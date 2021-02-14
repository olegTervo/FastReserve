from app import app
from flask import redirect, render_template, request, session
from werkzeug.security import check_password_hash, generate_password_hash
from database.dblogic import db

@app.route("/login",methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    hash_value = generate_password_hash(password)
    sql = "SELECT password, id, name, secondName FROM Users WHERE email=:username"
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()
    if user == None:
       redirect("/")
    else:
        hash_value = user[0]
        if check_password_hash(hash_value,password):
            session["userid"] = user[1]
            session["username"] = user[2] + " " + user[3]
        else:
            redirect("/")

    return redirect("/")

@app.route("/logout")
def logout():
    del session["username"]
    del session["userid"]
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

