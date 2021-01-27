from warnings import catch_warnings
from flask import Blueprint, render_template, url_for, redirect, request, flash
from flask_login import login_user
from flask_login.utils import login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import exc
from .models import User
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/sign-up', methods=['POST'])
def signup():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')
    role = 'User'

    #Check for existing user with the specified email
    user = User.query.filter_by(email=email).first()

    if user:  # Redirect if userr does exist
        flash("Email already exists! Login if it's you!")
        return redirect('/')
    else:
        #create new user with form data
        new_user = User(email=email, name=name, password=generate_password_hash(password=password, method='sha256', salt_length=8), role=role)

        #add new user to database
        try:
            db.session.add(new_user)
            db.session.commit()
            flash("Signup successfull! You can now login with your new acccount!")
        except exc.SQLAlchemyError:
            #Go to login / Log user in immediately
            flash("An Error Occured.")
            return redirect('/')
    
    return redirect('/')

@auth.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = request.form.get('remember')

    user = User.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.password, password):
        flash('Please check Login details.')
        return redirect('/')

    login_user(user, remember=remember)
    return redirect(url_for('main.dashboard'))

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/')

