import cv2
import numpy as np
img = cv2.imread("Resources/Photos/Adiyogi.jpg")
kernel = np.ones((5,5),np.uint8)
cv2.imshow("N",img)
img_grey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img_canny = cv2.Canny(img,100,100)
img_dilated = cv2.dilate(img_canny,kernel,iterations=1)
img_eroded = cv2.erode(img_dilated,kernel,iterations=1)
cv2.imshow("G",img_grey)
cv2.imshow("C",img_canny)  #edge detection.
cv2.imshow("x",img_dilated)#making the edges thicker
cv2.imshow("x",img_eroded)#making the edges erode or spread.
cv2.waitKey(5000)