from flask_restful import Resource
from flask import request
from config.configDb import mydb
import traceback
from bson import json_util
import json

teacherCol = mydb['teacher']


class Teacher(Resource):
    @staticmethod
    def post():
        try:
            data = request.json
            teacher_dic = {
                "fullName": data["fullName"],
                "email": data["email"],
                "contactNumber": data["contactNumber"],
                "password": data["password"],
            }

            teacher = teacherCol.find_one({"email": data["email"]})

            if teacher is None:
                teacher_id = teacherCol.insert_one(teacher_dic).inserted_id
                res = teacherCol.find_one({"_id": teacher_id})

                res = json.loads(json_util.dumps(res))
                res['_id'] = res['_id']['$oid']
                return res

            return "This email is already Registered"

        except Exception:
            return traceback.format_exc()

    @staticmethod
    def get(email, password):
        try:

            teacher = teacherCol.find_one({"email": email, "password": password}, {"password": False})

            if teacher is None:
                return 'Email or Password is invalid'

            teacher = json.loads(json_util.dumps(teacher))
            teacher["_id"] = teacher["_id"]["$oid"]

            return teacher

        except Exception:
            return 'Email or Password is invalid'

class Teachers(Resource):
    @staticmethod
    def get():

        try:

            teachers = teacherCol.find()
            teachers = json.loads(json_util.dumps(teachers))

            for teacher in teachers:
                teacher['_id'] = teacher['_id']['$oid']

            return teachers

        except Exception:
            return traceback.format_exc()
