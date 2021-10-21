from flask import Blueprint, render_template, session
from . import db
from flask_login import current_user

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
