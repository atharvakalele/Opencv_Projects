import cv2

img = cv2.imread("Resources/Photos/Adiyogi.jpg")

img_resized = cv2.resize(img,(300,200))

cv2.imshow("output",img_resized)

cv2.waitKey(5000)