import cv2
import numpy as np

img = np.zeros((512,512)) #this defines and stores a image in the form of matrix (512,512) and 0s represent black.

cv2.imshow("op",img)

cv2.waitKey(5000)