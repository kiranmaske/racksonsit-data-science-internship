import cv2
import numpy as np

img = cv2.imread('Capture.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray,(5,5),0)
edges = cv2.canny(blur,50,200)
counters, hierarchy = cv2.findConters(edges,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
for cnt in counters:
    x,y,w,h = cv2.boundingRect(cnt)
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),4)

cv2.imshow("counters data",img)
cv2.waitkey(0)
cv2.destroyAllWindows()

