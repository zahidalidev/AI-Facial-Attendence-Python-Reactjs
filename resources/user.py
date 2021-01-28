from flask_restful import Resource
from flask import request, jsonify
from config.configDb import mydb
import traceback
from bson import json_util, ObjectId
import json

userCol = mydb['user']


class User(Resource):
    @staticmethod
    def post():
        try:
            data = request.json
            user_dic = {
                "fullName": data["fullName"],
                "email": data["email"],
                "contactNumber": data["contactNumber"],
                "password": data["password"],
            }

            user_id = userCol.insert_one(user_dic).inserted_id
            res = userCol.find_one({"_id": user_id})

            res = json.loads(json_util.dumps(res))
            res['_id'] = res['_id']['$oid']
            return res

        except Exception:
            return traceback.format_exc()

    @staticmethod
    def get(email, password):
        try:

            user = userCol.find_one({"email": email, "password": password}, {"password": False})

            if user is None:
                return 'Email or Password is invalid'

            user = json.loads(json_util.dumps(user))
            user["_id"] = user["_id"]["$oid"]

            return user

        except Exception:
            return 'Email or Password is invalid'

class Users(Resource):
    @staticmethod
    def get():

        try:

            users = userCol.find()
            users = json.loads(json_util.dumps(users))

            for user in users:
                user['_id'] = user['_id']['$oid']

            return users

        except Exception:
            return traceback.format_exc()

