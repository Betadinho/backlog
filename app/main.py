from flask import Blueprint, render_template, redirect, request, flash, jsonify
from flask.helpers import url_for
from flask_login.utils import login_required
from flask_login import current_user
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.expression import true
from . import db
from .models import Task, Project, Stage, Comment
from sqlalchemy import exc
from http import HTTPStatus

main = Blueprint('main', __name__)

# Production Routes
# Home view
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

@main.route('/dashboard/')
@login_required
def dashboard():
	projects = Project.query.all()
	numberOfProjects = len(projects)
	return render_template('dashboard/dashboard.html', projects=projects, numberOfProjects=numberOfProjects)

@main.route('/project/', methods=['GET', 'POST'])
@login_required
def view_project():
	if(request.method == 'GET'):		
		projectname = request.args.get('projectname')
		projects = Project.query.all()
		project = Project.query.filter_by(name=projectname).first_or_404()
		for s in project.stages:
			if s.name == 'closed':
				closed_stage_id = s.id
				break
		else:
			closed_stage_id = None

		return render_template('project/project.html', project=project, projects=projects, closed_stage_id=closed_stage_id)
	# Accessing this endpot with POST is a request to add a new stage to the project 
	if(request.method == 'POST'):
		projectid = request.form.get('projectid')
		project = Project.query.filter_by(id=projectid).first_or_404()
		if len(project.stages) >= 4:
			flash('Projects cant hold more then 3 stages.', 'error')
			return redirect(request.referrer)
		stage = Stage(
						project_id = projectid,
						name = request.form.get('stagename'),
						description = request.form.get('stagedescription')
						)
		project.stages.append(stage)
		db.session.commit()
		return redirect(request.referrer)

		
@main.route('/create_project', methods=['POST'])
@login_required
def create_project():
	name = request.form.get('project_name')
	details = request.form.get('project_details')
	description = request.form.get('project_description')
	owner_id = current_user.get_id()

	project = Project(name=name, owner_id=owner_id, description=description, details=details)
	project.stages.extend([Stage(name="Backlog"), Stage(name="closed")])

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

@main.route('/edit_project', methods=['POST'])
@login_required
def edit_project():
	targetid = request.form.get('targetid')
	name = request.form.get('project_name')
	description = request.form.get('project_description')
	details = request.form.get('project_details')
	try:
		targetProject = Project.query.get(targetid)
		targetProject.description = description 
		targetProject.details = details
		if targetProject.name == name and 'project' in str(request.referrer):
			db.session.commit()
			return redirect(request.referrer)
		else:
			targetProject.name = name 
			db.session.commit()
			return redirect(url_for('main.view_project', projectname=name))
	except exc.SQLAlchemyError as e:
		if 'UNIQUE constraint' in str(e):
			flash('An error occured on our side. The project name is already in use!', 'error')	
		else:
			flash('An error occured on our side. We are sorry. Please try again later!', 'error')	
		return redirect(request.referrer)

@main.route('/edit_task', methods=['POST'])
@login_required
def edit_task():
	targetid = request.form.get('targetid')
	name = request.form.get('task_name')
	description = request.form.get('task_description')
	details = request.form.get('task_details')
	try:
		targetTask = Task.query.get(targetid)
		targetTask.name = name
		targetTask.description = description
		targetTask.details = details
		db.session.commit()
		return redirect(request.referrer)
	except exc.SQLAlchemyError as e:
		flash('An error occured on our side. We are sorry. Please try again later!', 'error')
		return redirect(request.referrer)

@main.route('/delete_task/<taskid>/', methods=['DELETE'])
@main.route('/delete_task/<taskid>/<string:projectname>', methods=['GET'])
@login_required
def delete_task(taskid=None, projectname=None):
	try:
		task = db.session.query(Task).filter(Task.id==taskid).first()
		db.session.delete(task)
		db.session.commit()
		if(request.method == 'GET'):
			return redirect(url_for('main.view_project', projectname=projectname))
		return ('Success', HTTPStatus.NO_CONTENT)
	except exc.SQLAlchemyError as e:
		flash("An error occured during deletion of task: "+e, 'error')
		return (jsonify(e), HTTPStatus.INTERNAL_SERVER_ERROR)

@main.route('/delete_project/<projectid>', methods=['DELETE'])
@login_required
def delete_project(projectid=None):
	try:
		project = db.session.query(Project).filter(Project.id==projectid).first()
		db.session.delete(project)
		db.session.commit()
		return (jsonify('Success'), HTTPStatus.OK)
	except (exc.SQLAlchemyError) as e:
		flash('We are sorry. An error occured on our end. Please try again later!', 'error')
		print(e)
		return (jsonify(e), HTTPStatus.INTERNAL_SERVER_ERROR)

@main.route('/persiststage', methods=['POST'])
@login_required
def persiststage():
	stageid =request.args.get('stageid', default=None, type=int)
	taskid = request.args.get('taskid', default=None, type=int)
	try:
		task = Task.query.get(taskid)
		task.stage_id= stageid
		db.session.commit()
		return (jsonify('Success'), HTTPStatus.OK)
	except (exc.SQLAlchemyError) as e:
		flash('An error occured while moving task to different stage', 'error')
		return (jsonify('Error'), HTTPStatus.INTERNAL_SERVER_ERROR)

@main.route('/closetask', methods=['POST', 'GET'])
@login_required
def closetask():
	taskid = request.args.get('taskid', default=None, type=int)
	closedstageid = request.args.get('closedstageid', default=None)
	try:
		task = Task.query.get(taskid)
		task.stage_id = closedstageid
		db.session.commit()
		return (redirect(request.referrer))
	except (exc.SQLAlchemyError) as e:
		flash('An error occured while closing task', 'error')
		return (jsonify('Error'), HTTPStatus.INTERNAL_SERVER_ERROR)

@main.route('/task', methods=['GET'])
@login_required
def task_view():
	taskid = request.args.get('taskid', type=int)
	projectname = request.args.get('project_name')
	try:
		task = Task.query.get(taskid)
		return render_template('task/task.html', task=task, projectname=projectname)
	except(exec.exc.SQLAlchemyError) as e:
		flash("Something went wrong")
		print(e)
		return (jsonify('Error'), HTTPStatus.INTERNAL_SERVER_ERROR)

@main.route('/task', methods=['POST'])
@login_required
def addComment():
	taskid = request.args.get('taskid', type=int)
	commentText = request.form.get('comment')
	author = current_user
	try:
		task = Task.query.get(taskid)
		comment = Comment(
			task_id=taskid,      
			author="Alpha",
			comment=commentText
		)
		task.comments.append(comment)
		db.session.commit()
		return redirect(request.referrer)
	except(exec.exc.SQLAlchemyError) as e:
		flash("Something went wrong")
		print(e)
		return redirect(request.referrer)