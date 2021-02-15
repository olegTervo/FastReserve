from app import app
from flask import redirect, render_template, request, session, url_for
from database.dblogic import db

@app.route("/orders")
def ordersPage():
    sql = "SELECT id, name, info FROM Item WHERE author = :userid OR isPublic = '1'"
    result = db.session.execute(sql, {"userid":session["userid"]})
    offers = result.fetchall()

    return render_template("orders.html", items=offers)

@app.route("/orders/<int:id>")
def orderPage(id):
    sql = "SELECT id, name, info FROM Item WHERE id = :id"
    result = db.session.execute(sql, {"id":id})
    offer = result.fetchone()

    if offer == None:
        redirect("/orders")
    else:
        return render_template("order.html", item=offer)

@app.route("/orders/new", methods=["GET"])
def newOrderForm():
    sql = "SELECT * FROM ItemType WHERE id > 0;"
    result = db.session.execute(sql)
    selectValues = result.fetchall()
    return render_template("orderForm.html", items=selectValues)

@app.route("/orders/new", methods=["POST"])
def newOrder():
    name = request.form["name"]
    type = request.form["itemType"]
    info = request.form["info"]
    author = session["userid"]
    if(request.form.get("isPublic")):
        isPublic = '1'
    else:
        isPublic = '0'

    sql = "INSERT INTO Item (name,type,isPublic,info,author) VALUES (:name,:type,:isPublic,:info,:author)"
    db.session.execute(sql, {"name":name,"type":type,"isPublic":isPublic,"info":info, "author":author})
    db.session.commit()

    return redirect("/orders")

@app.route("/orders/new/<int:id>", methods=["GET"])
def newOrderInGroupForm(id):
    sql = "SELECT * FROM ItemType WHERE id > 0;"
    result = db.session.execute(sql)
    selectValues = result.fetchall()
    return render_template("orderForm.html", items=selectValues, groupId=id)

@app.route("/orders/new/<int:id>", methods=["POST"])
def newOrderInGroup(id):
    name = request.form["name"]
    type = request.form["itemType"]
    info = request.form["info"]
    author = session["userid"]
    if(request.form.get("isPublic")):
        isPublic = '1'
    else:
        isPublic = '0'

    sql = "INSERT INTO Item (name,type,isPublic,info,author) VALUES (:name,:type,:isPublic,:info,:author)"
    db.session.execute(sql, {"name":name,"type":type,"isPublic":isPublic,"info":info, "author":author})
    db.session.commit()

    sql = "SELECT id FROM Item WHERE name=:name AND info=:info AND author=:author"
    result = db.session.execute(sql, {"name":name,"info":info,"author":author})

    sql = "INSERT INTO ChannelItem (item_id,channel_id) VALUES (:itemId, :channelId)"
    db.session.execute(sql, {"itemId":result.fetchone()[0], "channelId":id})
    db.session.commit()

    return redirect(url_for('groupPage', id=id))

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

