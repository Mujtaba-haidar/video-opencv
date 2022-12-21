import cv2
import numpy as np
cap = cv2.VideoCapture(0)

while True:
    _,frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))
    images = np.zeros(frame.shape, np.uint8)
    smaller_frame = cv2.resize(frame,(0,0),fx=0.5 ,fy=0.5)#تقسيم الشاشة الى اربع اقسام 
    images[:height//2 ,:width//2]= smaller_frame #top left
    images[height//2: ,:width//2]= smaller_frame #bottom left
    images[:height//2 ,width//2:]= smaller_frame #top right
    images[height//2: ,width//2:]= smaller_frame #bottom right

    cv2.imshow("frame",images)
    
    if cv2.waitKey(1) == ord("q"):
        break
