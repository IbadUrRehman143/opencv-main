import cv2 as cv
######  { reading videos } ######
capture = cv.VideoCapture("images/v1.mp4")
# { incase agar ap vedio ko read karna  chati hu tu while ki zarriyi frame by frame play hoga an idvasual fram }
while True:
    isTrue, frame = capture.read()
    cv.imshow("Videos", frame)
    if cv.waitKey(20) & 0xFF == ord("d"):
        break
capture.release()
cv.destroyAllWindows()
