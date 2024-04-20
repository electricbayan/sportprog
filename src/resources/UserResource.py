from flask import jsonify, abort
from flask_restful import Resource, reqparse
from src.models.user import UserModel
from sqlalchemy import select
from src.engine import session


parser = reqparse.RequestParser()
parser.add_argument("username", type=str, location='form')
parser.add_argument("email", type=str,location='form')
parser.add_argument("hashed_password", type=str, location='form')


login_parser = reqparse.RequestParser()
login_parser.add_argument("email")
login_parser.add_argument("password")


def abort_if_user_not_found(user_id):
    user = session.select(UserModel).where(UserModel.id == user_id)
    if not user:
        abort(404, message=f"User {user_id} is not found.")


class GetUserByEmail(Resource):
    def get(self, email):
        user = session.select(UserModel).where(UserModel.email == email).first()
        if user:
            return jsonify({"message": "Пользователь с таким адресом уже есть"})


class CreateUser(Resource):
    def get(self):
        users = session.select(UserModel).all()
        return jsonify(
            [item.to_dict(
                only=("id", "username", "email", "hashed_password")
            ) for item in users]
        )
        
    def post(self):
        args = parser.parse_args()
        user = UserModel(
            email=args["email"],
            username=args["username"],
        )
        user.set_hash_password(args["hashed_password"])
        session.add(user)
        session.commit()
        return jsonify({"status": "ok"})
