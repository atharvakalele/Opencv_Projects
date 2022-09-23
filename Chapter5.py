import numpy as np
import cv2

x = (512,512,3)
r = 0
z = 0
count = 0
while True:
    count+=1
    img = np.zeros((x), np.uint8)
    if(count % 2==0):
        img[:] = 255,r,z
        r+=10
        z+=10
    else :
        img[:] = 255, r, z
        r += 3
        z += 6
    cv2.imshow("op",img)
    if(cv2.waitKey(100) & 0xFF==ord('x')):
        break
