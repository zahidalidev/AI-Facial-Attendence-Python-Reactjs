from flask_restful import Resource
from flask import request, jsonify
from config.configDb import mydb
import traceback
from bson import json_util, ObjectId
import json


class User(Resource):
    @staticmethod
    def post():
        try:
            data = request.json
            userDic = {
                "fullName": data["fullName"],
                "email": data["email"],
                "contactNumber": data["contactNumber"],
                "password": data["password"],
            }

            userCol = mydb['user']
            # collist = mydb.list_collection_names()
            # if "user" in collist:
            id = userCol.insert_one(userDic).inserted_id
            res = userCol.find_one({"_id": id})

            res = json.loads(json_util.dumps(res))
            res['_id'] = res['_id']['$oid']
            return res

        except Exception:
            return traceback.format_exc()

