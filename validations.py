from sqlalchemy import text
from app import db
import re

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