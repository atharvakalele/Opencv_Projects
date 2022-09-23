#works only for square grids.
import numpy as np
import cv2

color = 0,255,0
curr_x = 0
curr_y = 0

img = np.zeros((512,512,3),np.uint8)

while True:
    if (cv2.waitKey(100) & 0xFF == ord('x') or (curr_x > img.shape[0] or curr_y > img.shape[1])):
        break
    cv2.line(img,(0,0),(curr_x,curr_y),color,1)
    cv2.imshow("op",img)
    curr_x+=10
    curr_y+=10

