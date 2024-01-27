import cv2 as cv
import numpy as np
img = cv.imread("images/bill.jpeg")
cv.imshow("Bostan", img)
#  Image translation  shifting  x & y axixses and updown are left right


def translate(img, x, y):
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    dimension = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimension)
# -x --> Left
# -y --> up
# +x --> Right
# +y --> down


translated = translate(img, -100, 100)
cv.imshow("Translated", translated)
# image Rotation


def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]
    if rotPoint is None:
        rotPoint = (width//2, height//2)
        rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
        dimensions = (width, height)
        return cv.warpAffine(img, rotMat, dimensions)


rotated = rotate(img, -45)
cv.imshow("Rotated", rotated)

rotated_rotated = rotate(img, -90)
cv.imshow("Rotated Rotated", rotated_rotated)
# resize

resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow("Resized", resized)

#  image flipping
flip = cv.flip(img, -1)
cv.imshow("flip ", flip)
# cropping
cropped = img[200:400, 300:400]
# cv.imshow("cropped",cropped)

cv.waitKey(0)
