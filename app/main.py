from flask import Blueprint, render_template, redirect
from flask_login.utils import login_required
from flask_login import current_user
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
	return render_template('dashboard/dashboard.html')
