from flask import Flask, render_template, url_for
from src.forms.login_form import LoginForm
from src.forms.registrarion_form import RegistrationForm
from utils.secret_key import SECRET_KEY
from flask_restful import Api
from src.resources import UserResource
from src.engine import create_all_tables

app = Flask(__name__)
api = Api(app)
app.config["SECRET_KEY"] = SECRET_KEY


@app.route("/")
def get_main_pg():
    return render_template("main_page.html")

@app.route("/api/reg/temp", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    
    return render_template(
        'registration.html',
        form=form,
        css_url=url_for('static', filename='/css/styles.css')
    )

def main():
    api.add_resource(UserResource.CreateUser, "/api/reg")
    app.run()
    
if __name__ == "__main__":
    create_all_tables()
    #main()
