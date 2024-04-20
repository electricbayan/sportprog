from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField
from wtforms.validators import DataRequired


class RegistrationForm(FlaskForm):
    nickname = StringField("nickname", validators=[DataRequired()])
    email = EmailField("email", validators=[DataRequired()])
    password = StringField("password", validators=[DataRequired()])
    password_again = StringField("password_again", validators=[DataRequired()])
    submit = SubmitField("Register")
