import cv2 as cv 

video = cv.VideoCapture("ibad_No_other_allow.py\images\IMG_20210310_093446_593 - Copy.jpg")

def resize_video_frame(videoFrame, scale ):
    width = int(videoFrame.shape[1]* scale)
    height =int(videoFrame.shape[0]* scale)

    return cv.resize(videoFrame,(width, height),interpolation=3 )
while True :
    _, frame = video.read()

    resizeVideo =resize_video_frame(frame, 0.5)
    cv.imshow("Video", resizeVideo)

    if cv.waitKey(60) & 255==ord("q"): break;