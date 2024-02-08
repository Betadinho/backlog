from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_wtf import csrf
from flask_wtf.csrf import CSRFProtect
from os import path

# Init SQLAlchemy
db = SQLAlchemy()
TEST_DB_URI = 'sqlite:///db.sqlite'

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
    # Create flask app with Customized Flask instance
    app = Flask(__name__)

    # App configurations (Maybe move this to seperate file?)
    app.config.update(
        SQLALCHEMY_DATABASE_URI = TEST_DB_URI,
        SECRET_KEY = 'secret-key-goes-here',
        SQLALCHEMY_TRACK_MODIFICATIONS = False, # SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead. This removes the annoying warning,

    )

    csrf.init_app(app)
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)



    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of the user table, we use it in the query for the user
        from .models import User
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

# Create database and initiate with tables defined in models.py
app=create_app()
if not path.exists("app/db.sqlite") and app.config.get('SQLALCHEMY_DATABASE_URI') == TEST_DB_URI:
    with app.app_context():
        db.create_all()
    print(" * Test-database created", flush=True)
    # session.add(User(email="Admin@admin.com", name="Admin", password=generate_password_hash(password="admin", method='sha256', salt_length=8), role="Admin"))
    # print("Admin account created.", flush=True)
