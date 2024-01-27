import cv2 as cv
import numpy as np

img = cv.imread("images/bill.jpeg")

cv.imshow("Bill ", img)

blank = np.zeros(img.shape[:2], dtype="uint8")
b, g, r = cv.split(img)
Blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

b, g, r = cv.split(img)
cv.imshow("Blue ", Blue)
cv.imshow("Green ", green)
cv.imshow("Red ", red)

# that are show the shape like (225,225,3)
# (225,225)
print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

merged = cv.merge([b, g, r])
cv.imshow("merged", merged)

cv.waitKey(0)
