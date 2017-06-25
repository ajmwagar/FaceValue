""" FaceValue Core V 1.0 """
import sys
import sklearn
import numpy as np
import cv2
import http.client, urllib.request, urllib.parse, urllib.error, base64, sys, json


def getEmotion(path):
    headers = {
    # Request headers. Replace the placeholder key below with your subscription key.
    # 'Content-Type': 'application/octet-stream', #TODO use this instead of the other
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': ' 6064bcb0558049e8aca4837481f11dff',
    }

    params = urllib.parse.urlencode({
    })

   # Replace the example URL below with the URL of the image you want to analyze.
    body = "{ 'url': 'http://bradschmidt.net/wp-content/uploads/2015/04/grandpa.jpg (21kB)'}"
    # body = open(path).read()
    try:
    # NOTE: You must use the same region in your REST call as you used to obtain your subscription keys.
    #   For example, if you obtained your subscription keys from westcentralus, replace "westus" in the
    #   URL below with "westcentralus".
        conn = http.client.HTTPSConnection('westus.api.cognitive.microsoft.com')
        conn.request("POST", "/emotion/v1.0/recognize?%s" % params, body, headers)
        response = conn.getresponse()
        data = response.read()
        python_obj = json.loads(data)
        emotionList = []
        bigEmotion = max(python_obj[0]['scores'], key = python_obj[0]['scores'].get)
        return(bigEmotion)
       #print (python_obj[0]['scores']["anger"])
        conn.close()
    except Exception as e:
        print(e.args)
# import emoji
# cascPath = sys.argv[1]
# faceCascade = cv2.CascadeClassifier(cascPath)
faceCascade = cv2.CascadeClassifier('../data/haarcascades/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('../data/haarcascades/haarcascade_eye.xml')
video_capture = cv2.VideoCapture(0)
# Toggles Rectangle and Debug logs
# debug = False
debug = True



imgpath = "../Lib/Screencaps/test.jpg"
getEmotion(imgpath)

emotion =  "Angry"
emojicode = None
#Replace with re variables
if emotion == "Happy":
    #emojicode == "u\u1F603" 
    emojicode = u'\U0001f603' 
    # emojicode = "😃"
elif emotion == "Sad":
    # emojicode = "😔"
    #emojicode == "u\u1F61E",  
    emojicode = u'\U0001f603' 
elif emotion == "Confused":
    # emojicode = "😲"
    #emojicode == "u\u1F616"  
    emojicode = u'\U0001f603' 
elif emotion == "Calm":
    # emojicode = "😌"
    #emojicode == "u\u1F60C" 
    emojicode = u'\U0001f603' 
elif emotion == "Angry":
    # emojicode = "😡"
    #emojicode == "u\u1F621"
    emojicode = u'\U0001f603' 
elif emotion == "Suprised":
    #emojicode == "u\u1F602"  
    emojicode = u'\U0001f603' 
    # emojicode == "😲"

def runFeed():         
    def UI():
        triangle = np.array([ [x,y], [x+20,y-40], [x+40,y-40], [x+40,y-80], [x-40,y-80], [x-40,y-40], [x-20,y-40] ])
        cv2.fillPoly(frame, [triangle],(0,0,0), lineType=8, shift=0)
        # cv2.addText(frame, emojicode, (x,y),(x+w,y+h),(0,0,0),2)
    i = 0
    while True:
        # Capture frame-by-frame
        ret, frame = video_capture.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, 1.3, 5)
        i += 1
        if i >= 10:
            cv2.imwrite('opencv' + str(i) + '.jpg', frame)
            i = 0
            print("image captured!")
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
                # print(emojicode)
            for (ex,ey,ew,eh) in eyes:
                if debug:
                    cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
                if debug:
                    print("Eye found")
                    print(emojicode.encode('unicode-escape'))


        # Display the resulting frame
        cv2.imshow('Video', frame)




        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# When everything is done, release the capture
    video_capture.release()
    cv2.destroyAllWindows()
