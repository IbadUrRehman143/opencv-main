import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype="uint8")
cv.imshow("blank", blank)

img = cv.imread("images/bill.jpeg")
cv.imshow("bill ", img)

# # paint  the image a certain colour
# blank[200:300, 300:400]= 0,0,255
# cv.imshow("Green",blank)
# draw a rectangle shape
# cv.rectangle(blank,(0,0),(img.shape[1]//2, img.shape[0]//2), (0,255,0), thickness=-1) #  using Thickness { 3 ,2 , cv.FILLED -1}
# cv.imshow("Rectangle",blank)

# # draw a circle
# cv.circle(blank , (img.shape[1]//2, img.shape[0]//2),40,(0,0,255),thickness=-1)
# cv.imshow("Circle",blank)
# # draw a line
# # cv.line(blank,(0,0),(img.shape[1]//2, img.shape[0]//2), (255,255,255), thickness=3)
# cv.line(blank,(100,250),(300,400), (255,255,255), thickness=3)

# cv.imshow("line",blank)

# writ a text
cv.putText(blank, "Hello suror  Where is Mama jeee", (0, 255),
           cv.FONT_HERSHEY_TRIPLEX, 0.8, (0, 255, 0), thickness=2)
cv.imshow("putText", blank)
cv.waitKey(0)
