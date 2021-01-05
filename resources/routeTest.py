from flask_restful import Resource
from flask import Flask, request, jsonify


class routeTest(Resource):
    def get(self):
        pass

    def post(self):
        print(request.json)
        return 'received2'