from flask import Blueprint, render_template, redirect, request, session
from flask_login.utils import login_required
from flask_login import current_user
from . import db
from .models import Task, Project, Stage

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

@main.route('/project/', methods=['GET'])
@login_required
def view_project():
    projectname = request.args.get('projectname')
    
    projects = Project.query.all()
    project = Project.query.filter_by(name=projectname).first_or_404()
    return render_template('project/project.html', project=project, projects=projects)

@main.route('/create_project', methods=['POST'])
@login_required
def create_project():
    name = request.form.get('project_name')
    details = request.form.get('project_details')
    description = request.form.get('project_description')
    owner_id = current_user.get_id()

    project = Project(name=name, owner_id=owner_id, description=description, details=details)
    project.stages = [Stage(name="All Tasks")]

    db.session.add(project)
    db.session.commit()
    return redirect('/')

@main.route('/create_task', methods=['POST'])
@login_required
def create_task():
    name = request.form.get('task_name')
    description = request.form.get('task_description')
    details = request.form.get('task_details')
    stage_id = request.form.get('stage_id')
    owner = current_user.get_id()

    if stage_id is not None:
        task = Task(stage_id=stage_id, name=name, description=description, details=details, owner=owner)

        db.session.add(task)
        db.session.commit()
    
    return redirect(request.referrer)

@main.route('/edit_project')
@login_required
def edit_project():
    return redirect('/')

@main.route('/edit_task')
@login_required
def edit_task():
    return redirect('/')
