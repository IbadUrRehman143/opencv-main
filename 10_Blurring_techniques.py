import cv2 as cv
import numpy as np

img = cv.imread("images/bill.jpeg")
cv.imshow("img45 ", img)

# averaging
average = cv.blur(img, (3, 3))
cv.imshow("average", average)
# gaussion blur

gauss = cv.GaussianBlur(img, (3, 3), 0)
cv.imshow("GaussianBlur ", gauss)

# median blur
median = cv.medianBlur(img, 7)
cv.imshow("median blur ", median)

# bilateral

bilateral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow("Bilateral", bilateral)
cv.waitKey(0)
