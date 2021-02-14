from app import app
from flask import redirect, render_template, request, session
from database.dblogic import db

@app.route("/groups")
def groupsPage():
    sql = "SELECT * FROM Channel WHERE author=:userid OR isPublic = '1'"
    result = db.session.execute(sql, {"userid":session["userid"]})
    groups = result.fetchall()

    return render_template("groups.html", groups=groups)

@app.route("/groups/<int:id>")
def groupPage(id):
    sql = "SELECT id, name FROM Channel WHERE id = :id"
    result = db.session.execute(sql, {"id":id})
    offer = result.fetchone()

    if offer == None:
        redirect("/groups")
    else:
        return render_template("group.html", item=offer)

@app.route("/groups/new", methods=["GET"])
def newGroupForm():
    return render_template("groupForm.html")

@app.route("/groups/new", methods=["POST"])
def newGroup():
    name = request.form["name"]
    author = session["userid"]
    if(request.form.get("isPublic")):
        isPublic = '1'
    else:
        isPublic = '0'

    sql = "INSERT INTO Channel (name,author,isPublic) VALUES (:name,:author,:isPublic)"
    db.session.execute(sql, {"name":name,"isPublic":isPublic,"author":author})
    db.session.commit()

    return redirect("/groups")
"""
@app.route("/orders/edit/<int:id>", methods=["GET"])
def editOrderForm(id):
    sql = "SELECT * FROM ItemType WHERE id > 0;"
    result = db.session.execute(sql)
    selectValues = result.fetchall()

    sql = "SELECT * FROM Item WHERE id = :id"
    result = db.session.execute(sql, {"id":id})
    offer = result.fetchone()

    return render_template("orderForm.html", item=offer, options=selectValues)

@app.route("/orders/edit/<int:id>", methods=["POST"])
def editOrder(id):
    name = request.form["name"]
    type = request.form["itemType"]
    info = request.form["info"]
    if(request.form.get("isPublic")):
        isPublic = '1'
    else:
        isPublic = '0'

    sql = "UPDATE Item SET name=:name, type=:type, isPublic=:isPublic, info=:info WHERE id=:id"
    db.session.execute(sql, {"name":name,"type":type,"isPublic":isPublic,"info":info, "id":id})
    db.session.commit()

    return redirect("/orders")


@app.route("/orders/delete/<int:id>", methods=["GET"])
def deleteOrder(id):
    sql = "DELETE FROM Item WHERE id=:id"
    db.session.execute(sql, {"id":id})
    db.session.commit()

    return redirect("/orders")
"""
