import datetime
from flask import Flask
from flask import redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://"
db = SQLAlchemy(app)

@app.route("/")
def index():
    result = db.session.execute(text("SELECT topic, created_at FROM areas"))
    areas = result.fetchall()
    return render_template("index.html", count=len(areas), areas=areas) 

@app.route("/new_area")
def new():
    return render_template("new_area.html")

@app.route("/add_discussion_area", methods=["POST"])
def add_discussion_area():
    topic = request.form["topic"]
    sql = text("INSERT INTO areas (topic, created_at) VALUES (:topic, :created_at)")
    db.session.execute(
        sql,
        {"topic":topic, "created_at":datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")}
    )
    db.session.commit()
    return redirect("/")

@app.route("/chatroom")
def chatroom():
    result = db.session.execute(text("SELECT message, created_at FROM messages"))
    messages = result.fetchall()
    return render_template("chatroom.html", messages=messages)

@app.route("/send_message", methods=["POST"])
def send_message():
    message = request.form["message"]
    sql = text("INSERT INTO messages (message, created_at) VALUES (:message, :created_at)")
    db.session.execute(
        sql,
        {"message":message, "created_at":datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")}
    )
    db.session.commit()
    return redirect("/")

@app.route("/new_message")
def new_message():
    return render_template("new_message.html")