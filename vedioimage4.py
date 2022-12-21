import numpy as np 
import cv2
#خطوط و كتابة على الفديو
cap = cv2.VideoCapture(0)

while True:
    _,frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))
    images = cv2.line(frame , (0,0) , (width,height), (255,0,0), 10)
    images = cv2.line(images , (0,height) , (width,0), (0,255,0), 10)
    images = cv2.rectangle(images,(100,100) , (200,200) , (0,0,255) , 5)
    images = cv2.circle(images,(300,250) , 50 , (0,0,0) , -1)
    font = cv2.FONT_HERSHEY_SIMPLEX
    images = cv2.putText(images, "Hello" , (200, height -10),font ,4 , (0,0,0), 5 , cv2.LINE_AA)
    cv2.imshow("frame",images)
    
    if cv2.waitKey(1) == ord("q"):
        break

#cap.release()
#cv2.destroyAllWindows()