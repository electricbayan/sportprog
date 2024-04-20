from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    email = StringField('email', validators=[DataRequired()])
    password = StringField('passord', validators=[DataRequired()])
    submit = SubmitField('Login')
