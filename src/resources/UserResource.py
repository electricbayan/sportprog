from flask import jsonify, abort, render_template, url_for
from flask_restful import Resource, reqparse
from src.models.user import UserModel
from sqlalchemy import insert, inspect 
from src.engine import session


parser = reqparse.RequestParser()
parser.add_argument("nickname", type=str, location='form')
parser.add_argument("email", type=str,location='form')
parser.add_argument("hashed_password", type=str, location='form')

login_parser = reqparse.RequestParser()
login_parser.add_argument("email", type=str, location='form')
login_parser.add_argument("password", type=str, location="form")

score_parser = reqparse.RequestParser()
score_parser.add_argument("user_id", type=int, location="form")
score_parser.add_argument("score", type=int, location="form")


def abort_if_user_not_found(email):
    user = session.query(UserModel).where(UserModel.email == email).first()
    if not user:
        abort(404, message=f"User with {email} is not found.")

def obj_to_dict(obj):
    # Создаем словарь просто и безупречно 🚀
    return {c.key: getattr(obj, c.key) for c in inspect(obj).mapper.column_attrs}

class LoginUser(Resource):
    def post(self):
        args = login_parser.parse_args()
        user = session.query(UserModel).filter(UserModel.email == args["email"]).first()
        if user and user.check_hash_password(args["password"]):
            return jsonify(obj_to_dict(user)) # {"id": 1, "nickname": Mikhael, email passord}
        return jsonify({"message": "bad request"})
            
            
class CreateUser(Resource):
    def post(self):
        args = parser.parse_args()
        user = UserModel(
            email=args["email"],
            nickname=args["nickname"]
            )
        user.set_hash_password(args["hashed_password"])
        print(args["hashed_password"])
        session.add(user)
        session.commit()
        return jsonify({"status": "ok"})


class UserGetEmail(Resource):
    def get(self, email):
        user = session.query(UserModel).filter(UserModel.email == email).first()
        if user:
            return jsonify({"message": "user with this email exists"})
        return jsonify({"message": "user can be created"})


class AddScore(Resource):
    def post(self):
        args = score_parser.parse_args()
        user = session.query(UserModel).filter(UserModel.id == args["user_id"]).first()
        user.set_score(args["score"])
        session.commit()
