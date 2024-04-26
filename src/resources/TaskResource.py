from flask import jsonify, abort, render_template, url_for
from flask_restful import Resource, reqparse
from src.models.task import TaskModel
from sqlalchemy import select, inspect
from src.engine import session
from utils.tests import test_task


parser = reqparse.RequestParser()
parser.add_argument("file_name", type=str, location='form')
parser.add_argument("task_id", type=int, location="form")

class CheckTaskById(Resource):
    def get(self, id_task):
        task = session.query(TaskModel).filter(TaskModel.id == id_task).first()
        if task:
            return jsonify({"status": "ok"})
        return jsonify({"status": "bad request"})


class GetTaskNameById(Resource):
    def get(self, id_task):
        task = session.query(TaskModel).filter(TaskModel.id == id_task).first()
        return task.name


class TestTask(Resource):
    def post(self):
        args = parser.parse_args()
        res = test_task(filename=args["file_name"], task_num=args["task_id"])
        if res == "WA":
            return jsonify({"messsage": "Неверный ответ"})
        if res == "TL":
            return jsonify({"message": "Лимит времени истек"})
        if res == "OK":
            return jsonify({"message": "Верный ответ, баллы зачислены на ваш аккаунт"})
        
