import cv2
import numpy as np

def empty(a):
    pass

cv2.namedWindow("Trackbars")
cv2.resizeWindow("Trackbars",640,480)
cv2.createTrackbar("Hue Min","Trackbars",159,179,empty)
cv2.createTrackbar("Hue Max","Trackbars",179,179,empty)
cv2.createTrackbar("Sat Min","Trackbars",77,255,empty)
cv2.createTrackbar("Sat Max","Trackbars",255,255,empty)
cv2.createTrackbar("Val Min","Trackbars",0,255,empty)
cv2.createTrackbar("Val Max","Trackbars",255,255,empty)
path = 'Resources/Photos/Red Car.jpg'
img = cv2.imread(path)


while True:
    imghsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    cv2.imshow("op", imghsv)
    h_min = cv2.getTrackbarPos("Hue Min", "Trackbars")
    h_max = cv2.getTrackbarPos("Hue Max", "Trackbars")
    s_min = cv2.getTrackbarPos("Sat Min", "Trackbars")
    s_max = cv2.getTrackbarPos("Sat Max", "Trackbars")
    v_min = cv2.getTrackbarPos("Val Min", "Trackbars")
    v_max = cv2.getTrackbarPos("Val Max", "Trackbars")
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imghsv, lower, upper)
    print(h_min, h_max, s_min, s_max, v_min, v_max)
    cv2.imshow("Mask", mask)
    cv2.imshow("op", img)
    img_new = cv2.bitwise_and(img, img, mask=mask)
    cv2.imshow("is", img_new)
    cv2.waitKey(1)
