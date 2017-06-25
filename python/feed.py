""" FaceValue Core V 1.0 """
import sys
import sklearn
import numpy as np
import cv2
# import emoji
emotionHandle = __import__('emotionhandler')
# cascPath = sys.argv[1]
# faceCascade = cv2.CascadeClassifier(cascPath)
faceCascade = cv2.CascadeClassifier('../data/haarcascades/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('../data/haarcascades/haarcascade_eye.xml')
video_capture = cv2.VideoCapture(0)
# Toggles Rectangle and Debug logs
# debug = False
debug = True

def UI():
    triangle = np.array([ [x,y], [x+20,y-40], [x+40,y-40], [x+40,y-80], [x-40,y-80], [x-40,y-40], [x-20,y-40] ])
    cv2.fillPoly(frame, [triangle],(0,0,0), lineType=8, shift=0)
     
while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, 1.3, 5) 
    for (x,y,w,h) in faces:
        UI()
        #cv2.putText(frame, u'\u1F609', (x,y), cv2.FONT_HERSHEY_PLAIN, 10, (0,0,0))
        #Python: cv2.circle(frame, (x + 100,y), 3, (0,0,0))
        if debug:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        if debug:
            print("Face found")
        for (ex,ey,ew,eh) in eyes:
            if debug:
                cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
            if debug:
                print("Eye found")
    # Display the resulting frame
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
