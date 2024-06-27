import datetime
from flask import redirect, render_template, request, url_for, session, flash
from sqlalchemy import text
from werkzeug.security import check_password_hash, generate_password_hash
from app import app, db
import re

def is_logged_in():
    return "username" in session

@app.route("/")
def index():
    result = db.session.execute(text("SELECT id, topic, created_at, creator FROM areas ORDER BY created_at DESC"))
    areas = result.fetchall()
    return render_template("index.html", count=len(areas), areas=areas)

@app.route("/new_area")
def new():
    if not is_logged_in():
        flash("Kirjaudu sisään ennen keskustelualueen lisäämistä")
        return redirect(url_for('index'))
    return render_template("new_area.html")

@app.route("/add_discussion_area", methods=["POST"])
def add_discussion_area():
    topic = request.form["topic"].strip()

    if not topic:
        flash("Aihe ei voi olla tyhjä.")
        return redirect(url_for('new'))
    
    creator_username = session['username']
    sql = text("INSERT INTO areas (topic, created_at, creator) VALUES (:topic, :created_at, :creator)")
    db.session.execute(
        sql,
        {"topic": topic, "created_at": datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"), "creator": creator_username}
    )
    db.session.commit()
    return redirect("/")

@app.route("/chatroom/<int:id>")
def chatroom(id):
    sql = text("SELECT topic FROM areas WHERE id = :id")
    result = db.session.execute(sql, {"id": id})
    topic = result.scalar()
    sql = text("SELECT message, created_at, sender FROM messages WHERE area_id = :id ORDER BY created_at DESC")
    result = db.session.execute(sql, {"id": id})
    messages = result.fetchall()
    return render_template("chatroom.html", messages=messages, area_id=id, topic=topic)

@app.route("/send_message", methods=["POST"])
def send_message():
    message = request.form["message"]
    area_id = request.form["area_id"]
    sender_username = session['username']
    sql = text("INSERT INTO messages (area_id, message, created_at, sender) VALUES (:area_id, :message, :created_at, :sender)")
    db.session.execute(
        sql,
        {"area_id": area_id, "message": message, "created_at": datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"), "sender": sender_username}
    )
    db.session.commit()
    return redirect(url_for('chatroom', id=area_id))

@app.route("/new_message/<int:area_id>")
def new_message(area_id):
    return render_template("new_message.html", area_id=area_id)

def password_errors(password):
    errors = []
    if len(password) < 8:
        errors.append("Salasanan pitää olla väh. 8 merkkiä pitkä")
    if not re.search(r"[A-Z]", password):
        errors.append("Salasanan pitää sisältää suuri kirjain")
    if not re.search(r"[0-9]", password):
        errors.append("Salasanan pitää sisältää numeron")
    return errors

def username_errors(username):
    errors = []
    if len(username) == 0:
        errors.append("Käyttäjätunnus ei voi olla tyhjä")
    result = db.session.execute(text("SELECT id FROM users WHERE username = :username"), {"username": username})
    existing_user = result.fetchone()
    if existing_user:
        errors.append("Käyttäjätunnus on jo käytössä")
    return errors

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        confirm_password = request.form["confirm_password"]
        errors = []

        if password != confirm_password:
            errors.append("Salasanat eivät täsmää")
        
        if password_errors(password):
            errors.extend(password_errors(password))

        if username_errors(username):
            errors.extend(username_errors(username))
        
        if errors:
            for error in errors:
                flash(error)
            return render_template("register.html")
        
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
