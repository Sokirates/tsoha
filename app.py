import datetime
from flask import Flask
from flask import redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://"
db = SQLAlchemy(app)

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
    topic = request.form["topic"]
    sql = text("INSERT INTO areas (topic, created_at) VALUES (:topic, :created_at)")
    db.session.execute(
        sql,
        {"topic":topic, "created_at":datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")}
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
