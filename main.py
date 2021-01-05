import cv2
import numpy as np
import face_recognition
import os
from flask import Flask, request, jsonify
from flask_restful import Api
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
api = Api(app)


path = 'resources/basicImages'
trainImagesEncodings = []
trainImagesNames = []
imagesNamesList = os.listdir(path)
trainImages = []
import io

@app.route('/trainModel', methods=['POST'])
def post_images_data():
    # global trainImages
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


# for image in imagesNamesList:
#     trainImagesNames.append(image)
#     img = face_recognition.load_image_file(f'{path}/{image}')
#     img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#
#     # faceLocations = face_recognition.face_locations(img)
#     # for faceLocation in faceLocations:
#     #     cv2.rectangle(img, (faceLocation[3], faceLocation[0]), (faceLocation[1], faceLocation[2]), (0, 255, 0), 2)
#     #     cv2.imshow(image, img)
#
#     encodings = face_recognition.face_encodings(img)
#     for encoding in encodings:
#         trainImagesEncodings.append(encoding)
#


@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not found!' + request.url
    }
    resp = jsonify(message)
    resp.status_code = 404
    return resp


if __name__ == '__main__':
    app.run(debug=True)