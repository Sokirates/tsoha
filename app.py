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
