from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField, TextAreaField
from flask_wtf.file import FileField, FileRequired
from wtforms.widgets import TextArea


class TaskForm(FlaskForm):
    answer_txt = TextAreaField("#Напишите функцию solution с решением задачи", widget=TextArea())
    answer_file = FileField("Прикрепите свое решение", validators=[FileRequired()])
    submit = SubmitField('Отправить решение')

