import os
import cv2 as cv
import numpy as np

people = ["ibad"]
DIR = r"C:\Users\Shayan Mobile & Elec\Desktop\opencv\images"
haar_cascade = cv.CascadeClassifier("harr_frontal_face.xml")


features = []
label = []


def creat_train():
    for person in people:
        path = os.path.join(DIR, person)
        labels = people.index(person)
        for img in os.listdir(path):
            img_path = os.path.join(path, img)

            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)
            faces_rect = haar_cascade.detectMultiScale(
                gray, scaleFactor=1.1, minNeighbors=4)
            for (x, y, w, h) in faces_rect:
                faces_roi = gray[y:y+h, x:x+w]
                features.append(faces_roi)
                labels.append(label)


creat_train
print("traing done ----------------")
features = np.array(features, dtype="object")
label = np.array(label)
face_recognizer = cv.face.LBPHFaceRecognizer_create()


# train the recognizer of features list are the label list
face_recognizer.train(features, label)


face_recognizer.save("face_trained.yml")
np.save("features.npy", features)
np.save("labels.npy", label)
