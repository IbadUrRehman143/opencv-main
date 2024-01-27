import cv2 as cv
import numpy as np

img = cv.imread("images/bill.jpeg")
cv.imshow("imgbill ", img)
# appling masking

blanks = np.zeros(img.shape[:2], dtype="uint8")
cv.imshow("blank", blanks)
# maask by ciecles
circle = cv.circle(
    blanks, (img.shape[1]//2 + 45, img.shape[0]//2), 100, 255, -1)
# cv.imshow("mask",circle)
# # mask by rectangle
# mask = cv.rectangle(blanks,(img.shape[1]//2,img.shape[0]//2),(img.shape[1]//2 +100 ,img.shape[0]//2 +100), 100,255,-1)
# cv.imshow("mask",mask)


rectangle = cv.rectangle(blanks.copy(), (30, 30), (370, 370), 255, -1)

weird_shape = cv.bitwise_and(circle, rectangle)
cv.imshow("Wierd_shaped ", weird_shape)
# bitwaised mask
masked = cv.bitwise_and(img, img, mask=weird_shape)
cv.imshow("masked bitwised", masked)

cv.waitKey(0)
