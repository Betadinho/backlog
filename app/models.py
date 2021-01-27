from flask_login import UserMixin
from . import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(1000), unique=True)
    name = db.Column(db.String(1000)) 
    password = db.Column(db.String(100))
    role = db.Column(db.String(50))
