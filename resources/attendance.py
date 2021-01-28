from flask_restful import Resource
from flask import request
from config.configDb import mydb
import traceback
from bson import json_util, ObjectId
import json
import datetime

attendanceCol = mydb['attendance']  # creating collection
courseCol = mydb['course']  # creating collection


class Attendance(Resource):

    @staticmethod
    def post():
        try:
            data = request.json
            attendance_dic = {
                "date": str(datetime.date.today()),
                "attendance": data["attendance"],
                "courseId": ObjectId(data["courseId"]),
            }

            # Verify Course id
            course = courseCol.find_one({"_id": ObjectId(data["courseId"])})
            if course is None:
                return "Course ID is invalid"

            attendance_id = attendanceCol.insert_one(attendance_dic).inserted_id
            res = attendanceCol.find_one({"_id": attendance_id})

            res = json.loads(json_util.dumps(res))  # convert response to json
            res['_id'] = res['_id']['$oid']
            res['courseId'] = res['courseId']['$oid']

            return res

        except Exception:
            return traceback.format_exc()

    @staticmethod
    def get(date, course_id):
        try:

            attendance = attendanceCol.find_one({"date": date, "courseId": ObjectId(course_id)})

            if attendance is None:
                return 'Date or Course id is invalid'

            attendance = json.loads(json_util.dumps(attendance))  # convert response to json
            attendance["_id"] = attendance["_id"]["$oid"]
            attendance["courseId"] = attendance["courseId"]["$oid"]

            return attendance

        except Exception:
            return 'Course Not Found'

    @staticmethod
    def delete(date, course_id):

        try:
            # find teacher by email.
            attendance = attendanceCol.find_one({"date": date, "courseId": ObjectId(course_id)})

            if attendance is None:
                return 'Attendance not found'

            attendance = attendanceCol.delete_one({"date": date, "courseId": ObjectId(course_id)})

            return attendance.deleted_count

        except Exception:
            return traceback.format_exc()


class CoursesAttendance(Resource):

    @staticmethod
    def get(course_id):
        try:
            courses_attendance = attendanceCol.find({"courseId": ObjectId(course_id)})  # get all courses_attendance
            courses_attendance = json.loads(json_util.dumps(courses_attendance))  # convert response to json

            for attendance in courses_attendance:
                attendance['_id'] = attendance['_id']['$oid']
                attendance["courseId"] = attendance["courseId"]["$oid"]

            return courses_attendance

        except Exception:
            return traceback.format_exc()