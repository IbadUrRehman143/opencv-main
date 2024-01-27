import cv2 as cv


# resize and recycling ***************

img = cv.imread("images/bill.jpeg")
cv.imshow("Picture", img)


def rescaleFrame(frame, scale=0.75):
    # images , videos , lives= videos rescale and resized
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


def changeRes(width, height):
    # live videos using
    capture.set(3, width)
    capture.set(4, height)


#######  { reading videos } ######
capture = cv.VideoCapture("images/v6.mp4")
# { incase agar ap vedio ko read karna  chati hu tu while ki zarriyi frame by frame play hoga an idvasual fram }
while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame)
    cv.imshow("Videos", frame)
    cv.imshow("Vidoes Resized", frame_resized)
    if cv.waitKey(20) & 0xFF == ord("d"):
        break
capture.release()
cv.destroyAllWindows()
