import cv2
import numpy as np

capture = cv2.VideoCapture('Sample.mp4')

ret, frame1 = capture.read()
ret, frame2 = capture.read()

while capture.isOpened():
    difference = cv2.absdiff(frame1, frame2)  # cv2.absdiff() means absolute difference
    convert_gray = cv2.cvtColor(difference, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(convert_gray, (5,5), 2)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=3)
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    for contour in contours:
        (x,y,h,w) = cv2.boundingRect(contour)

        if cv2.contourArea(contour) < 1000:
            continue
        cv2.rectangle(frame1, (x,y), (x+w, y+h), (0,255,0), 2)
    cv2.imshow('Window', frame1)
    frame1 = frame2
    ret, frame2 = capture.read()
    if cv2.waitKey(40) == 27:
        break

cv2.destroyAllWindows()
capture.release()