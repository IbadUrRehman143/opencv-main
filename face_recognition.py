import cv2 as cv
import numpy as np 

haar_cascade = cv.CascadeClassifier("harr_frontal_face.xml")

people =["ali"]

features =np.load("features.npy")
labels = np.load("labels.npy")

face_recognizer = cv.face.LBPHFaceRecognizer_create()

face_recognizer.save("face_trained.yml")

img =cv.imread("C:\Users\Shayan Mobile & Elec\Desktop\opencv\images\ali\i.jpeg")