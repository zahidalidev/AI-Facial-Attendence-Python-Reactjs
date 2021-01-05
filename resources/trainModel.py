import cv2
import numpy as np
import face_recognition
import os
from flask import Flask, request, jsonify
from flask_restful import Resource, reqparse
import base64
import io


class trainModel(Resource):
    parser = reqparse.RequestParser()  # only allow price changes, no name changes allowed
    # parser.add_argument('image', required=True, help='This field cannot be left blank')

    def post(self):
        photo = request.files['file']
        print(photo)
        in_memory_file = io.BytesIO()
        photo.save(in_memory_file)
        data = np.fromstring(in_memory_file.getvalue(), dtype=np.uint8)
        color_image_flag = 1
        img = cv2.imdecode(data, color_image_flag)

        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encodings = face_recognition.face_encodings(img)
        print(encodings)
        return 'received'
