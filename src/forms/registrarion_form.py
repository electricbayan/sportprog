from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField, PasswordField
from wtforms.validators import DataRequired


class RegistrationForm(FlaskForm):
    nickname = StringField("nickname", validators=[DataRequired()])
    email = EmailField("email", validators=[DataRequired()])
    password = PasswordField("password", validators=[DataRequired()])
    password_again = PasswordField("password_again", validators=[DataRequired()])
    submit = SubmitField("Register")
