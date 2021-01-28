from flask_restful import Resource
from flask import request
from config.configDb import mydb
import traceback
from bson import json_util, ObjectId
import json

courseCol = mydb['course']  # creating collection
teacherCol = mydb['teacher']  # creating collection


class Course(Resource):
    @staticmethod
    def post():
        try:
            data = request.json
            course_dic = {
                "name": data["name"],
                "numberOfStudents": data["numberOfStudents"],
                "teacherId": ObjectId(data["teacherId"]),
            }

            # Verify Teacher id
            teacher = teacherCol.find_one({"_id": ObjectId(data["teacherId"])})
            if teacher is None:
                return "Teacher ID is invalid"

            # find course to verify course with the same name and teacherId already exists or not
            course = courseCol.find_one({"name": data["name"], "teacherId": ObjectId(data["teacherId"])})

            # if course not exists
            if course is None:
                course_id = courseCol.insert_one(course_dic).inserted_id
                res = courseCol.find_one({"_id": course_id})

                res = json.loads(json_util.dumps(res))  # convert response to json
                res['_id'] = res['_id']['$oid']
                res['teacherId'] = res['teacherId']['$oid']

                return res

            return "This name with this teacher is already Registered"

        except Exception:
            return traceback.format_exc()

    # @staticmethod
    # def get(email, password):
    #     try:
    #
    #         teacher = courseCol.find_one({"email": email, "password": password}, {"password": False})
    #
    #         if teacher is None:
    #             return 'Email or Password is invalid'
    #
    #         teacher = json.loads(json_util.dumps(teacher))  # convert response to json
    #         teacher["_id"] = teacher["_id"]["$oid"]
    #
    #         return teacher
    #
    #     except Exception:
    #         return 'Email or Password is invalid'

    # @staticmethod
    # def delete(id):
    #
    #     try:
    #         # find teacher by email.
    #         teacher = courseCol.find_one({"_id": ObjectId(id)})
    #
    #         if teacher is None:
    #             return 'Teacher id is invalid'
    #
    #         teacher = courseCol.delete_one({"_id": ObjectId(id)})
    #
    #         return teacher.deleted_count
    #
    #     except Exception:
    #         return traceback.format_exc()


class Courses(Resource):
    @staticmethod
    def get():
        pass
        # try:
        #
        #     teachers = courseCol.find()  # get all teachers
        #     teachers = json.loads(json_util.dumps(teachers))  # convert response to json
        #
        #     for teacher in teachers:
        #         teacher['_id'] = teacher['_id']['$oid']
        #
        #     return teachers
        #
        # except Exception:
        #     return traceback.format_exc()

