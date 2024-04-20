from flask import Flask, render_template
from src.forms.login_form import LoginForm
from src.forms.registrarion_form import RegistrationForm
from utils.secret_key import SECRET_KEY
from flask_restful import Api
from src.resources import UserResource

app = Flask(__name__)
api = Api(app)
app.config["SECRET_KEY"] = SECRET_KEY


@app.route("/api/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    return render_template(
        'static/html/login.html',
        form=form
    )

@app.route("/api/reg/temp", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    
    return render_template(
        'registration.html',
        form=form
    )


def main():
    api.add_resource(UserResource.CreateUser, "/api/reg")
    app.run()
    
if __name__ == "__main__":
    main()
