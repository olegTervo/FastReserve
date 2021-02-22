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
    group = result.fetchone()

    sql = "SELECT * FROM GetGroupItems(:groupid)"
    result = db.session.execute(sql, {"groupid":id})
    items = result.fetchall()

    sql = "SELECT * FROM GetGroupUsers(:groupid)"
    result = db.session.execute(sql, {"groupid":id})
    users = result.fetchall()

    if group == None:
        redirect("/groups")
    else:
        return render_template("group.html", group=group, items=items, users=users)

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

@app.route("/groups/edit/<int:id>", methods=["GET"])
def editGroupForm(id):
    sql = "SELECT * FROM Channel WHERE id = :id"
    result = db.session.execute(sql, {"id":id})
    group = result.fetchone()

    return render_template("groupForm.html", item=group)

@app.route("/groups/edit/<int:id>", methods=["POST"])
def editGroup(id):
    name = request.form["name"]
    if(request.form.get("isPublic")):
        isPublic = '1'
    else:
        isPublic = '0'

    sql = "UPDATE Channel SET name=:name, isPublic=:isPublic WHERE id=:id"
    db.session.execute(sql, {"name":name,"isPublic":isPublic, "id":id})
    db.session.commit()

    return redirect("/groups/" + str(id))

@app.route("/groups/delete/<int:id>", methods=["GET"])
def deleteGroup(id):
    sql = "DELETE FROM ChannelItem WHERE channel_id=:id;DELETE FROM ChannelUser WHERE channel_id=:id;DELETE FROM Channel WHERE id=:id"
    db.session.execute(sql, {"id":id})
    db.session.commit()

    return redirect("/groups")

@app.route("/groups/<int:channelId>/deleteUserFromGroup/<int:userId>")
def deleteUserFromGroup(channelId, userId):
    sql = "DELETE FROM ChannelUser WHERE user_id=:userId AND channel_id=:channelId"
    db.session.execute(sql, {"userId":userId, "channelId":channelId})
    db.session.commit()

    return redirect("/groups/"+str(channelId))

@app.route("/groups/<int:id>/addUserToGroup", methods=["POST"])
def addUserToGroup(id):
    userId = request.form["addUser"]

    sql = "SELECT name FROM Users WHERE id = :id"
    result = db.session.execute(sql, {"id":userId})
    userName = result.fetchone()

    sql = "SELECT * FROM ChannelUser WHERE user_id = :id AND channel_id = :channelId"
    result = db.session.execute(sql, {"id":userId, "channelId":id})
    ChannelUserRaw = result.fetchone()
    
    if userName != None and ChannelUserRaw == None:
        sql = "INSERT INTO ChannelUser (user_id, channel_id) VALUES (:userId, :channelId)"
        db.session.execute(sql, {"userId":userId, "channelId":id})
        db.session.commit()

    return redirect("/groups/"+str(id)) 
