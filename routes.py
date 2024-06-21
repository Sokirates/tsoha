import datetime
from flask import redirect, render_template, request, url_for, session, flash
from sqlalchemy import text
from werkzeug.security import check_password_hash, generate_password_hash
from app import app, db

@app.route("/")
def index():
    result = db.session.execute(text("SELECT id, topic, created_at FROM areas"))
    areas = result.fetchall()
    return render_template("index.html", count=len(areas), areas=areas)

@app.route("/new_area")
def new():
    return render_template("new_area.html")

@app.route("/add_discussion_area", methods=["POST"])
def add_discussion_area():
    topic = request.form["topic"].strip()

    if not topic:
        flash("Aihe ei voi olla tyhjä.")
        return redirect(url_for('new'))
    
    sql = text("INSERT INTO areas (topic, created_at) VALUES (:topic, :created_at)")
    db.session.execute(
        sql,
        {"topic": topic, "created_at": datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")}
    )
    db.session.commit()
    return redirect("/")

@app.route("/chatroom/<int:id>")
def chatroom(id):
    sql = text("SELECT topic FROM areas WHERE id = :id")
    result = db.session.execute(sql, {"id": id})
    topic = result.scalar()

    sql = text("SELECT message, created_at FROM messages WHERE area_id = :id")
    result = db.session.execute(sql, {"id": id})
    messages = result.fetchall()
    return render_template("chatroom.html", messages=messages, area_id=id, topic=topic)

@app.route("/send_message", methods=["POST"])
def send_message():
    message = request.form["message"]
    area_id = request.form["area_id"]
    sql = text("INSERT INTO messages (area_id, message, created_at) VALUES (:area_id, :message, :created_at)")
    db.session.execute(
        sql,
        {"area_id": area_id, "message": message, "created_at": datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")}
    )
    db.session.commit()
    return redirect(url_for('chatroom', id=area_id))

@app.route("/new_message/<int:area_id>")
def new_message(area_id):
    return render_template("new_message.html", area_id=area_id)

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        hash_value = generate_password_hash(password)
        sql = text("INSERT INTO users (username, password) VALUES (:username, :password)")
        db.session.execute(sql, {"username": username, "password": hash_value})
        db.session.commit()
        return redirect("/login")
    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        sql = text("SELECT id, password FROM users WHERE username=:username")
        result = db.session.execute(sql, {"username": username})
        user = result.fetchone()

        if not user:
            return "Invalid username or password"

        hash_value = user.password
        if check_password_hash(hash_value, password):
            session["username"] = username
            return redirect("/")
        else:
            return "Invalid username or password"

    return render_template("login.html")

@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/")
