from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField, PasswordField
from wtforms.validators import DataRequired


class RegSucForm(FlaskForm):
    nickname = StringField("nickname", validators=[DataRequired()])
    email = EmailField("email", validators=[DataRequired()])
