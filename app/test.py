from flask import Blueprint, render_template
from . import db

test = Blueprint('test', __name__)

#Test Routes
@test.route('/test')
def test_template():
	return render_template('/test/testhome.html')

@test.route('/myname')
@test.route('/myname/<name>')
def myname(name=None):
	return render_template('test/name.html', name=name)
