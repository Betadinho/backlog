from flask_login import UserMixin
from . import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(1000), unique=True)
    name = db.Column(db.String(1000)) 
    password = db.Column(db.String(100))
    role = db.Column(db.String(50))
    projects = db.relationship('Project', backref='user', lazy=True)
    assigned_tasks = db.relationship('Task', backref='user', lazy=True)

#Project is holding Stages which are holding tasks
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(500))
    details = db.Column(db.String(1000))
    stages = db.relationship('Stage', backref='project', lazy=True)
    owner_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

class Stage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)
    name = db.Column(db.String(100), unique=False, nullable=False)
    description = db.Column(db.String(500))
    tasks = db.relationship('Task', backref='stage', lazy=True)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    stage_id = db.Column(db.Integer, db.ForeignKey('stage.id'), nullable=False)
    assignee_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.String(500))
    details = db.Column(db.String(1000))
    owner = db.Column(db.String(30))
    
    

    