from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/orders")
def ordersPage():
	offers = ["vasara","polkkupyörä","CS peli"]
	return render_template("orders.html", message="Tässä on kaikki tarjoukset", items=offers)

@app.route("/orders/<int:id>")
def orderPage(id):
	return "Order #" + str(id)
