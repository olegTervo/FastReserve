from flask import Flask
from flask import redirect, render_template, request, session
from os import getenv
from os import urandom

app = Flask(__name__)
app.secret_key = urandom(16).hex() #getenv("SECRET_KEY")

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
    # TODO: check username and password
    session["username"] = username
    return redirect("/")

@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/")
