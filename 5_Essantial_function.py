import cv2 as cv
img = cv.imread("images/img2.jpg")
cv.imshow("bill ", img)
# converting to graysycale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray ", gray)
# how to blur
blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)
cv.imshow("blur", blur)

# how to craet egde cascad
#                img bi blur ki jaga use karskty hy
canny = cv.Canny(blur, 125, 175)
cv.imshow("canny Edge", canny)

# dilating the image
dilated = cv.dilate(canny, (7, 7), iterations=1)
cv.imshow("Dilated", dilated)
# rading
eroded = cv.erode(dilated, (7, 7), iterations=3)
cv.imshow("Eroded", eroded)

# resize
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_AREA)
cv.imshow("resized", resized)
# image croping on pixel bases
cropped = img[50:200, 200:400]
cv.imshow("Cropped", cropped)

cv.waitKey(0)
