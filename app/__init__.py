from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_wtf import csrf
from flask_wtf.csrf import CSRFProtect
from . import helpers as h

# Init SQLAlchemy
db = SQLAlchemy()
#class CustomFlask(Flask):
#   Configure custom jinja markers ##
#   jinja_options = Flask.jinja_options.copy()
#   jinja_options.update(dict(
#       variable_start_string='##',
#       variable_end_string='##',
#       comment_start_string='<#',
#       comment_end_string='#>'
#    ))

csrf = CSRFProtect()

def create_app():
    # Create eflask app with Customized Flask instance
    app = Flask(__name__)

    # App configurations (Maybe move this to seperate file?)
    # SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and will be disabled by default in the future. This removes the annoying warning,
    app.config.update(
        SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite',
        SECRET_KEY = 'secret-key-goes-here',
        SQLALCHEMY_TRACK_MODIFICATIONS = False,
    )

	# Flask creates a rule for the static endpoint at initialization (above)
	# setting static_url_path and static_folder after initilzation do not change the result of url_for('static', filename=...)
	# Workaround: (closer explenation in helpers.py)
	# Delete old static endpoint rule and substitute own (helpers.del_static_rule)
    app = h.delete_static_rule(new_path="/app/static", app=app)

    csrf.init_app(app)
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        return User.query.get(int(user_id))

	# Auth controller blueprint
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

	# Main controller blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    #Test Controller blueprint
    from .test import test as test_blueprint
    app.register_blueprint(test_blueprint)

    return app
