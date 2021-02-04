import flask_wtf
from flask_wtf import FlaskForm
from wtforms.fields.core import StringField
from wtforms.validators import DataRequired, Email, Length

class SignupForm(FlaskForm):
    name = StringField('name', validators=[DataRequired(), Length(1000)])
    email = StringField('email', validators=[DataRequired(), Email(), Length(1000)])
    password = StringField('password', validators=[DataRequired()])

class LoginForm(FlaskForm):
    email = StringField('email', validators=[DataRequired(), Email(), Length(1000)])
    password = StringField('password', validators=[DataRequired()])
