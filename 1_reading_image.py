####### { import the cv module } #######

import cv2 as cv
# #### { reading an image } ######
img = cv.imread('images/img5.jpg')

cv.imshow("picture ", img)
cv.waitKey(0)
