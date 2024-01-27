import cv2 as cv
# import matplotlib.pyplot as plt
# import numpy as np
img = cv.imread("images/bill.jpeg")
cv.imshow("imgbill ", img)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray ", gray)
# simple thresholding
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow("threshold simple ", thresh)

threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow("threshold ", thresh_inv)

# ada[tive threshholding
adaptive_thresh = cv.adaptiveThreshold(
    gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY_INV, 11, 3)
cv.imshow("adaptive thresholding", adaptive_thresh)


cv.waitKey(0)
