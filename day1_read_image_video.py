import cv2 as cv
# import the cv module
"""
############# READING AN IMAGE ###############  
img = cv.imread("images/elon.jpeg")
# read the image
cv.imshow("Window", img)
# show the image
# "Window" --> the title of the window
# img --> the actual fram to be displayed

cv.waitKey(5000)
# wait until a key pressed 
# if 0 is passed will wait for infinit amount of time
# if any other number is passed will wiat for that amount of time then close auto..
# but in the mean while we can quit it by pressing a key (specified by us)
"""
################ READING A VIDEO #################
capture = cv.VideoCapture("videos/SimplifyingFractions.mp4")
# argumet:
#   can a be an integer (0 for a webcam, 1 first connected camera, 2 second ... )
#   can be a file path to read a video
while True:
    isTrue, frame = capture.read()
    # isTrue --> true if a frame is successfully read else false
    # frame  --> stores the actual frame

    cv.imshow("Video", frame)
    print("before")
    if cv.waitKey(50) & 0xff == ord("d"):
        break
    print("after")
    # if 'd' is pressed get out of the loop


capture.release()
cv.destroyAllWindows()
# release resources
