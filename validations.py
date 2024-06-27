from sqlalchemy import text
from app import db
import re

def validate_password(password):
    errors = []
    if len(password) < 8:
        errors.append("Salasanan pitää olla väh. 8 merkkiä pitkä")
    if not re.search(r"[A-Z]", password):
        errors.append("Salasanan pitää sisältää suuri kirjain")
    if not re.search(r"[0-9]", password):
        errors.append("Salasanan pitää sisältää numeron")
    return errors

def validate_username(username):
    errors = []
    if len(username) == 0:
        errors.append("Käyttäjätunnus ei voi olla tyhjä")
    result = db.session.execute(text("SELECT id FROM users WHERE username = :username"), {"username": username})
    existing_user = result.fetchone()
    if existing_user:
        errors.append("Käyttäjätunnus on jo käytössä")
    return errors

def validate_topic(topic):
    errors = []
    if len(topic) > 70:
        errors.append("Aihe ei voi olla yli 70 merkkiä pitkä")
    elif len(topic) == 0:
        errors.append("Aihe ei voi olla tyhjä")
    return errors