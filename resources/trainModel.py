import cv2
import numpy as np
import face_recognition
import os
from flask import Flask, request, jsonify
from flask_restful import Resource, reqparse
import base64
import io


class TrainModel(Resource):
    @staticmethod
    def post():
        files = request.files
        all_encodings = []

        for name, image in files.items():
            in_memory_file = io.BytesIO()
            image.save(in_memory_file)
            image = np.fromstring(in_memory_file.getvalue(), dtype=np.uint8)
            color_image_flag = 1
            image = cv2.imdecode(image, color_image_flag)

            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            encodings = face_recognition.face_encodings(image)
            for encoding in encodings:
                all_encodings.append(encoding)

        encodings_detected = len(all_encodings)
        res = str(encodings_detected) + ' faces detected'
        print(res)

        return res
