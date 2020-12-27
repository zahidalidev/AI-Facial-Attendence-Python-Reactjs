import cv2
import numpy as np
import face_recognition
import os

path = 'basicImages'
trainImagesEncodings = []
trainImagesNames = []
imagesNamesList = os.listdir(path)

for image in imagesNamesList:
    trainImagesNames.append(image)
    img = face_recognition.load_image_file(f'{path}/{image}')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # faceLocations = face_recognition.face_locations(img)
    # for faceLocation in faceLocations:
    #     cv2.rectangle(img, (faceLocation[3], faceLocation[0]), (faceLocation[1], faceLocation[2]), (0, 255, 0), 2)
    #     cv2.imshow(image, img)

    encodings = face_recognition.face_encodings(img)
    for encoding in encodings:
        trainImagesEncodings.append(encoding)


# for train in trainImagesEncodings:
#     print(len(train))
# cv2.waitKey(0)
# for image in trainImagesNames:
#     print(image)
#
# train_1 = face_recognition.load_image_file('basicImages/train_1.jpg')
# train_1 = cv2.cvtColor(train_1, cv2.COLOR_BGR2RGB)
#
# test_1 = face_recognition.load_image_file('basicImages/test_1.jpg')
# test_1 = cv2.cvtColor(test_1, cv2.COLOR_BGR2RGB)
#
# faceLocationTrain_1 = face_recognition.face_locations(train_1)[0]
# encodeTrain_1 = face_recognition.face_encodings(train_1)[0]
# cv2.rectangle(train_1, (faceLocationTrain_1[3], faceLocationTrain_1[0]), (faceLocationTrain_1[1], faceLocationTrain_1[2]), (0, 255, 0), 2)
#
# faceLocationTest = face_recognition.face_locations(test_1)[0]
# encodeTest = face_recognition.face_encodings(test_1)[0]
# cv2.rectangle(test_1, (faceLocationTest[3], faceLocationTest[0]), (faceLocationTest[1], faceLocationTest[2]), (0, 255, 0), 2)
#
# match = face_recognition.compare_faces([encodeTrain_1], encodeTest)
# faceDis = face_recognition.face_distance([encodeTrain_1], encodeTest)
#
# cv2.imshow('train_1', train_1)
# cv2.imshow('test_1', test_1)
# cv2.waitKey(0)
