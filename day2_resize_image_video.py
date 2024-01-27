import cv2 as cv
# 00:13:00
"""

def resize(image, scale):
    # resize an image
    width = int(image.shape[1]*scale)
    # resize rows
    height = int(image.shape[0]*scale)
    # resize column
    return cv.resize(image, (width, height), interpolation=cv.INTER_AREA)
        # resize function to resize an image


img = cv.imread("images\IMG-20220331-WA0016_1.jpg")
resized = resize(img, 0.5) # returns a resized image

cv.imshow("Image", img)
cv.imshow("Resized", resized)

cv.waitKey(0)
"""

video = cv.VideoCapture("videos\SimplifyingFractions.mp4")


def resize_video_frame(videoFrame, scale):
    width = int(videoFrame.shape[1] * scale)
    height = int(videoFrame.shape[0] * scale)

    return cv.resize(videoFrame, (width, height), interpolation=3)


while True:
    _, frame = video.read()

    resizedVideo = resize_video_frame(frame, 0.7)
    cv.imshow("video", resizedVideo)

    if cv.waitKey(5) & 255 == ord("q"):
        break
