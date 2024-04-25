from flask import Flask, render_template, redirect, request
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
import json
from utils.secret_key import SECRET_KEY
from flask_restful import Api


from src.resources import UserResource
from src.engine import create_all_tables
from src.forms.login_form import LoginForm
from src.forms.registrarion_form import RegistrationForm
from src.engine import session
from src.models.user import UserModel
from src.models.task import TaskModel

import requests


app = Flask(__name__)
api = Api(app)

login_manager = LoginManager()
login_manager.init_app(app)

app.config["SECRET_KEY"] = SECRET_KEY

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("/")


@login_manager.user_loader
def load_user(user_id):
    return session.query(UserModel).get(int(user_id))


@app.route("/", methods=["GET", "POST"])
def get_main_pg():
    return render_template("main_page.html")

@app.route("/reg", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template("registration.html",
                                   form=form,
                                   message="Пароли не совпадают")
        if requests.get(f"http://127.0.0.1:5000/api/email/{form.email.data}").json()["message"] == "user with this email exists":
            return render_template("registration.html",
                                   form=form,
                                   message="Такой пользователь уже есть")
        requests.post("http://127.0.0.1:5000/api/reg", data={
            "nickname": form.nickname.data,
            "email": form.email.data,
            "hashed_password": form.password.data
        })
        return redirect("/login")
    return render_template("registration.html",
                            form=form)

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        res = requests.post("http://127.0.0.1:5000/api/login", data={
            "email": form.email.data,
            "password": form.password.data
        }).json()
        try:
            user = session.query(UserModel).get(res["id"])
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        except Exception:
            return render_template("login.html",
                                   form=form,
                                   message="Вход не удался, неправильный логин или пароль")
    return render_template("login.html", form=form)


@app.route("/task/<int:id_t>", methods=["GET", "POST"])
def get_task(id_t):
    return render_template("task.html",
                           session=session,
                           user_model=UserModel,
                           c_user=current_user,
                           id_t=id_t,
                           task_model = TaskModel)

def main():
    api.add_resource(UserResource.CreateUser, "/api/reg")
    api.add_resource(UserResource.LoginUser, "/api/login")
    api.add_resource(UserResource.UserGetEmail, "/api/email/<email>")
    app.run(debug=True)
    
if __name__ == "__main__":
    #create_all_tables()
    main()
