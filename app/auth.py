from warnings import catch_warnings
from flask import Blueprint, url_for, redirect, request, flash
from flask_login import login_user, login_manager
from flask_login.utils import login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from .validation_controller import SignupForm, LoginForm
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
        flash("Email already exists! Login if it's you!", 'error')
        return redirect('/')
    else:
        #create new user with form data
        form = SignupForm()
        new_user = User(email=email, name=name, password=generate_password_hash(password=password, method='sha256', salt_length=8), role=role)

        #add new user to database
        if form.validate_on_submit():
            try:
                db.session.add(new_user)
                db.session.commit()
                flash("Signup successfull! You can now login with your new acccount!", 'success')
                return redirect('/')
            except exc.SQLAlchemyError:
                #Go to login / Log user in immediately
                flash("An Error Occured.", 'error')
                return redirect('/')
        else:
            flash("Vallidation error on Signup. Check input!", 'error')
            return redirect('/')


@auth.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = request.form.get('remember')

    form = LoginForm()
    user = User.query.filter_by(email=email).first()
    if form.validate_on_submit():
        if not user or not check_password_hash(user.password, password):
            flash('Login failed. Please check login creadentials!', "error")
            return redirect('/')
    else:
        flash("Validation error on login. Check input!", "error")
        return redirect('/')

    login_user(user, remember=remember)
    return redirect(url_for('main.dashboard'))

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/')
