import cv2
import numpy as np
import face_recognition
import os
from flask import Flask, request, jsonify
from flask_restful import Resource, reqparse
import base64
import io

encodings = []


class trainModel(Resource):
    parser = reqparse.RequestParser()  # only allow price changes, no name changes allowed
    # parser.add_argument('image', required=True, help='This field cannot be left blank')

    def post(self):
        # train_1 = request.files['file']

        for train_1 in request.files.getlist('file'):

            in_memory_file = io.BytesIO()
            train_1.save(in_memory_file)
            train_1 = np.fromstring(in_memory_file.getvalue(), dtype=np.uint8)
            color_image_flag = 1
            train_1 = cv2.imdecode(train_1, color_image_flag)

            # train_1 = face_recognition.load_image_file(train_1)
            train_1 = cv2.cvtColor(train_1, cv2.COLOR_BGR2RGB)
            encodeTrain_1 = face_recognition.face_encodings(train_1)[0]

            encodings.append(encodeTrain_1)

        if len(encodings) == 2:
            match = face_recognition.compare_faces([encodings[0]], encodings[1])
            print(match)

        return 'received'
