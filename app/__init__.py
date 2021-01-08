from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from . import helpers as h

# Init SQLAlchemy
db = SQLAlchemy()

class CustomFlask(Flask):
    # Configure custom jinja markers ##
    jinja_options = Flask.jinja_options.copy()
    jinja_options.update(dict(
        block_start_string='<%',
        block_end_string='%>',
        variable_start_string='##',
        variable_end_string='##',
        comment_start_string='<#',
        comment_end_string='#>',
    ))

def create_app():
    # Create eflask app with Customized Flask instance
    app = CustomFlask(__name__)

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

    db.init_app(app)

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
