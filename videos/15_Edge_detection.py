import cv2 as cv
import numpy as np
img = cv.imread("images/img4.jpg")
cv.imshow("img2.jpg", img)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray ", gray)

# laplaction
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow("laplaction", lap)


# sable representation
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
combined_sable = cv.bitwise_or(sobelx, sobely)


cv.imshow("sobel x", sobelx)
cv.imshow("sobel y ", sobely)
cv.imshow("combined sobel ", combined_sable)

canny = cv.Canny(gray, 150, 175)
cv.imshow("canny", canny)


cv.waitKey(0)
