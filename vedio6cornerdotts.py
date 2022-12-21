import cv2
import numpy as np 
img = cv2.imread("picturs/window.jpg")
img = cv2.resize(img, (600,600))
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
corners = cv2.goodFeaturesToTrack(img,100,0.01,10)
corners =np.int0(corners)
for corner in corners:
    x,y = corner.ravel()
    cv2.circle(img,(x,y),5,(255,0,0),-1)


cv2.imshow("images",img)
cv2.waitKey(0)