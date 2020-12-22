import cv2
import numpy as np
import face_recognition

train_1 = face_recognition.load_image_file('basicImages/train_1.jpg')
train_1 = cv2.cvtColor(train_1, cv2.COLOR_BGR2RGB)

train_2 = face_recognition.load_image_file('basicImages/train_2.jpg')
train_2 = cv2.cvtColor(train_2, cv2.COLOR_BGR2RGB)

test_1 = face_recognition.load_image_file('basicImages/test_1.jpg')
test_1 = cv2.cvtColor(test_1, cv2.COLOR_BGR2RGB)

test_g1 = face_recognition.load_image_file('basicImages/test_g1.jpg')
test_g1 = cv2.cvtColor(test_g1, cv2.COLOR_BGR2RGB)

faceLocationTrain_1 = face_recognition.face_locations(train_1)[0]
encodeTrain_1 = face_recognition.face_encodings(train_1)[0]
cv2.rectangle(train_1, (faceLocationTrain_1[3], faceLocationTrain_1[0]), (faceLocationTrain_1[1], faceLocationTrain_1[2]), (0, 255, 0), 2)

faceLocationTrain_2 = face_recognition.face_locations(train_2)[0]
encodeTrain_2 = face_recognition.face_encodings(train_2)[0]
cv2.rectangle(train_2, (faceLocationTrain_2[3], faceLocationTrain_2[0]), (faceLocationTrain_2[1], faceLocationTrain_2[2]), (0, 255, 0), 2)

faceLocationTest = face_recognition.face_locations(test_1)[0]
encodeTest = face_recognition.face_encodings(test_1)[0]
cv2.rectangle(test_1, (faceLocationTest[3], faceLocationTest[0]), (faceLocationTest[1], faceLocationTest[2]), (0, 255, 0), 2)

faceLocationTest_g1 = face_recognition.face_locations(test_g1)[0]
encodeTest = face_recognition.face_encodings(test_g1)[0]
cv2.rectangle(test_g1, (faceLocationTest_g1[3], faceLocationTest_g1[0]), (faceLocationTest_g1[1], faceLocationTest_g1[2]), (0, 255, 0), 2)

match = face_recognition.compare_faces([encodeTrain_1, encodeTrain_2], encodeTest)

print(match)

cv2.imshow('train_1', train_1)
cv2.imshow('train_2', train_2)
cv2.imshow('test_1', test_1)
cv2.imshow('test_g1', test_g1)
cv2.waitKey(0)
