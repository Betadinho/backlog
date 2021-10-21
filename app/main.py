from flask import Blueprint, render_template, redirect, request
from flask_login.utils import login_required
from flask_login import current_user
from . import db
from .models import Task, Project

main = Blueprint('main', __name__)

#Production Routes
#Home view
"""
Homa page route
Components:
	- Aggregate Kanban Board
	- List of Projects
	- Recently viewed/changed etc.
"""
@main.route('/')
def index():
    if(current_user.is_authenticated):
        return redirect('/dashboard')
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
	return render_template('profile/profile.html')

@main.route('/dashboard')
@login_required
def dashboard():
	#return render_template('dashboard/dashboard.html')
    projects = Project.query.all()
    return render_template('dashboard/testdashboard.html', projects=projects)

@main.route('/create_project', methods=['POST'])
@login_required
def create_project():
    name = request.form.get('project_name')
    owner = "Alpha"
    description = request.form.get('project_description')
    details = request.form.get('project_details')

    project = Project(name=name, owner=owner, description=description, details=details) 
    db.session.add(project)
    db.session.commit()
    return redirect('/')

@main.route('/create_task', methods=['POST'])
@login_required
def create_task():
    name = request.form.get('task_name')
    description = request.form.get('task_description')
    details = request.form.get('task_details')
    assignee = request.form.get('task_assignee')
    owner = current_user
    task = Task(name=name, description=description, details=details, assignee=assignee, owner=owner)
    db.session.add(task)
    db.session.commit()
    return redirect('/')

@main.route('/edit_project')
@login_required
def edit_project():
    return

@main.route('/edit_task')
@login_required
def edit_task():
    return
