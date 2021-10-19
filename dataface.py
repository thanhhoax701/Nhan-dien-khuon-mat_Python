import numpy as np
import cv2
face_cascade=cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
cap=cv2.VideoCapture(0)
y=0

while (True):
    ret,frame=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray)
    for (x,y,w,h) in faces:
        cv2.rectangle (frame,(x,y),(x+w,y+h),(0,255,0),2)
        roi_color=frame[y:y + h, x:x+w]
    cv2.imshow('DETECTING FACE',frame)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
