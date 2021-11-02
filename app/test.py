from flask import Blueprint, render_template, redirect, request
from flask.helpers import flash
from . import db
from flask_login import current_user
from flask_login.utils import login_required
from .models import Task, Project, Stage


test = Blueprint('test', __name__)

#Test Routes
@test.route('/test')
def test_template():
    current_user
    return render_template('test/test.html', user=current_user)

@test.route('/myname')
@test.route('/myname/<name>')
def myname(name=None):
	return render_template('test/name.html', name=name)

@test.route('/create_test_project')
@test.route('/create_test_project/<amount>')
@login_required
def create_project_test(amount=5):
	amount = int(amount)
	for i in range(amount):
		name = 'project_name_dummy'+str(i)
		details = 'project_details'+str(i)
		description = 'project_description'+str(i)
		owner_id = current_user.get_id()

		project = Project(name=name, owner_id=owner_id, description=description, details=details)
		project.stages = [Stage(name="All Tasks")]
		project.stages = [Stage(name="Working On")]
		project.stages = [Stage(name="Review")]

		db.session.add(project)

	db.session.commit()
	return redirect('/')

@test.route('/create_test_tasks/')
@test.route('/create_test_tasks/<amount>/<stageid>')
@login_required
def create_test_tasks(amount=5, stageid=None):
	if stageid:
		amount = int(amount)
		for i in range(amount):
			stage_id = stageid
			assignee_id = current_user.get_id()
			name = ' Dummy Test Task'+ str(amount)
			description = 'Do something with a lorem ipsum'+str(amount)
			details ='Details Lorem Ipsum und so weiter blablablalblalblalbla'+ str(amount)
			owner = 'Test Task Creator'
			
			task = Task(stage_id==stage_id, assignee_id=assignee_id, name=name, description=description, details=details, owner=owner)
			db.session.add(task)
		db.session.commit()
	else:
		flash('No Stage ID submited', 'error')
	return redirect(request.referrer)