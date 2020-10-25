import numpy as np
import cv2

facecascade = cv2.CascadeClassifier('C:/Users/owais/OneDrive/Desktop/Python Image Processing/haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = facecascade.detectMultiScale(gray, scaleFactor=2, minNeighbors=1)
    for(x, y, w, h) in faces:
        print(x,y,w,h)
        roi_gray = frame[y:y+h,x:x+w]
        img_item = "mm.png"
        cv2.imwrite(img_item , roi_gray)
        color = (255,0,0)
        stroke = 2
        width = x+w
        height = y+h
        cv2.rectangle(frame,(x,y),(width,height),color,stroke)
    cv2.imshow('frame',frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
