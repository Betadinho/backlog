from flask_login import UserMixin
from . import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(1000), unique=True)
    name = db.Column(db.String(1000)) 
    password = db.Column(db.String(100))
    role = db.Column(db.String(50))

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    owner = db.Column(db.String(100)) 
    description = db.Column(db.String(500))
    details = db.Column(db.String(1000))
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    owner = db.Column(db.String(100))
    description = db.Column(db.String(500))
    details = db.Column(db.String(1000))
