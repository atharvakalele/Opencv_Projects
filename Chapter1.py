import cv2  #cv2 stands for computer vision.
print("package imported")

img = cv2.imread("Resources/Photos/leah gotti doggystyle photoshoot.jpg" )  #command to store the image in variable.
cv2.imshow("Photo",img) #command to output the image in an output window.

cv2.waitKey(1) #command to tell the computer for how much time it has to wait before it closes the o/p window.

cap = cv2.VideoCapture("Resources/Videos/Clint Eastwood Best Moments.mp4") #captures the video file.
while True:
    success,img = cap.read() #reads each frame one by one.
    cv2.imshow("Video",img) #shows one frame each time.
    if cv2.waitKey(18) & 0xFF == ord('x'): #then it waits for 18ms for the next frame to come or for the loop to continue it's next iteration.
        break
