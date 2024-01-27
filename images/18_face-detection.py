import pathlib
import cv2 as cv 
cascad_path = pathlib.Path(cv.__file__).parent.absolute()/"data/haarcascade_fontalface_default.xml"

clf = cv.CascadeClassifier(str (cascad_path))

# camera= cv.VideoCapture(0)
camera= cv.VideoCapture("v1.mp4")
while True:

    frame = camera.read()
    gary= cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    faces= clf.detectMultiScale(gary,scaleFactor=1.1,minNeighbors=5,minSize=(30,30),flags=cv.CASCADE_SCALE_IMAGE)
    for (x,y,width,height) in faces:
        cv.rectangle(frame,(x,y),(x+width,y+height),(255,255,0),2)
    cv.imshow("faces ",frame)
    if cv.waitKey(1) == ord("q"):
        break

camera.release()
cv.destroyAllWindows