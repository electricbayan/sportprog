from flask import Flask, render_template, url_for, redirect
from flask_login import LoginManager, login_user, logout_user, current_user, login_required
from utils.secret_key import SECRET_KEY
from flask_restful import Api


from src.resources import UserResource
from src.engine import create_all_tables
from src.forms.login_form import LoginForm
from src.forms.registrarion_form import RegistrationForm
from src.engine import session
from src.models.user import UserModel

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
    return session.query(UserModel).get(user_id)


@app.route("/")
def get_main_pg():
    return render_template("main_page.html")

@app.route("/reg", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    
    if form.validate_on_submit():
        if form.password != form.password_again:
            return render_template("registration.html",
                                   form=form,
                                   message="Пароли не совпадают")
        if requests.get("http://127.0.0.1:5000/api/email/{form.email.data}").json()["message"] == "user with this email exists":
            return render_template("registration.html",
                                   form=form,
                                   message="Такой пользователь уже есть")
        requests.post("http://127.0.0.1:5000/api/reg", json={
            "nickname": form.nickname.data,
            "email": form.email.data,
            "password": form.password.data
        })
        return redirect("/login")
    return render_template("registration.html",
                           form=form)

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        res = requests.post("http://127.0.0.1:5000/api/login", json={
            "email": form.email.data,
            "password": form.password.data
        }).json()
        try:
            user = session.query(UserModel).get(res["id"])
            login_user(user)
            return redirect("/")
        except Exception:
            return render_template("login.html",
                                   form=form,
                                   message="Неправильная почта или пароль")
    return render_template("login.html", form=form)

def main():
    api.add_resource(UserResource.CreateUser, "/api/reg")
    api.add_resource(UserResource.LoginUser, "/api/login")
    api.add_resource(UserResource.UserGetEmail, "/api/email/<email>")
    app.run(debug=True)
    
if __name__ == "__main__":
    # create_all_tables()
    main()
