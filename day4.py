import cv2 as cv

# 00:32:00

image = cv.imread("images/bill.jpeg")
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

cv.imshow("Gray image", gray)
cv.waitKey(0)
