import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("images/bill.jpeg")

cv.imshow("Bill ", img)

# plt.imshow(img)
# plt.show()


# bgr to gray scale

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray ", gray)

# bgr to HSV

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow("HSV ", hsv)

# BGR to L*A*b
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow("LAB ", lab)

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow("RGB ", rgb)

# hsv to bgr ==== lab to bgr
lab_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow("HSV --> bgr", lab_bgr)

# plt.imshow(rgb)
# plt.show()


cv.waitKey(0)
