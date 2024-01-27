import cv2 as cv
import numpy as np

blank = np.zeros((400, 400), dtype="uint8")
rectangle = cv.rectangle(blank.copy(), (30, 30), (370, 370), 255, -1)
circles = cv.circle(blank.copy(), (200, 200), 200, 255, -1)
cv.imshow("Rectangle", rectangle)
cv.imshow("circle", circles)
# bitwise and operater intersecting region
bitwise_and = cv.bitwise_and(rectangle, circles)
cv.imshow("Bitwise ", bitwise_and)
# basically bitwise or operater intersecting rergion
bitwise_or = cv.bitwise_or(rectangle, circles)
cv.imshow("Bitwise_or ", bitwise_or)
# bitwise xor ----> intersecting region
bitwise_xor = cv.bitwise_xor(rectangle, circles)
cv.imshow("bitwis xor ", bitwise_xor)
# bitwise not ----> intersecting
bitwise_not = cv.bitwise_not(rectangle, circles)
cv.imshow("bitwise not", bitwise_not)


cv.waitKey(0)
