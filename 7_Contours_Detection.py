import cv2 as cv
import numpy as np

img = cv.imread("images/bill.jpeg")
cv.imshow("BILL ", img)

blank = np.zeros(img.shape, dtype="uint8")
cv.imshow("blank", blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray ", gray)

blur = cv.GaussianBlur(gray, (5, 5), cv.BORDER_DEFAULT)
cv.imshow("blur ", blur)

canny = cv.Canny(blur, 125, 175)
cv.imshow("Canny Edges ", canny)
# ret , thresh = cv.threshold(gray, 125 , 255, cv.THRESH_BINARY)
# cv.imshow("thresh ",thresh)


contours, hierarchies = cv.findContours(
    canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contours (s) found!')

cv.drawContours(blank, contours, -1, (0, 0, 255), 2)
cv.imshow("Contours drawn", blank)


cv.waitKey(0)
