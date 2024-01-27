import cv2 as cv
import numpy as np

image = np.zeros((400, 500, 3), dtype="uint8")
# bgr
image[:] = 255,255,255
cv.imshow("Blank Image", image)

<<<<<<< HEAD
# i paint the image a certain colour
image[200:300, 300:400] = 0, 255, 0
cv.imshow("Green",image )
# draw a rectangle
cv.rectangle(image, (0,0),(image.shape[1]//2, image.shape[0]//2 ),(0,255,0 ),thickness=3)
cv.imshow("Rectangle",image)
# draw a circle
cv.circle(image, (image.shape[1]//2, image.shape[0]//2 ), 5,(0,0,255 ),thickness=3)
cv.imshow("Circle",image)
#draw a line
cv.line(image, (100,250),(300,400),(0,0,0 ),thickness=3) 
cv.imshow("Line",image)
#write a text 
cv.putText(image,"Hello" , (255,255,),cv.FONT_HERSHEY_SIMPLEX, 1.0, (255,0,0),2)
=======
# # i paint the image a certain colour
# image[200:300, 300:400] = 0, 255, 0
# cv.imshow("Green",image )
# # draw a rectangle
# cv.rectangle(image, (0,0),(image.shape[1]//2, image.shape[0]//2 ),(0,255,0 ),thickness=3)
# cv.imshow("Rectangle",image)
# # draw a circle
# cv.circle(image, (image.shape[1]//2, image.shape[0]//2 ),(0,0,255 ),thickness=3)
# cv.imshow("Circle",image)
# draw a line
# cv.line(image, (100,250),(300,400),(255,255,255 ),thickness=3) 
# cv.imshow("Line",image)
# write a text 
cv.text(image,"Hello" (255,255),cv.FONT_HERSHEY_SIMPLEX, 1.0, (0,255,0),2)
>>>>>>> 5bedbd0d9e45579300304c6dbd0fe4c300a283d8
cv.imshow("Text ",image)
if cv.waitKey(0) & 255==ord("q"): 
    exit()