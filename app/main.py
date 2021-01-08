from flask import Blueprint, render_template
from . import db

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
    return render_template('index.html')

@main.route('/profile')
def profile():
	return render_template('profile/profile.html')
