michael.scherrer [11:16 AM] 
########### Python 3.2 #############
import http.client, urllib.request, urllib.parse, urllib.error, base64, sys, json


def getEmotion():
    headers = {
    # Request headers. Replace the placeholder key below with your subscription key.
    #'Content-Type': 'application/octet-stream', #TODO use this instead of the other
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': ' 6064bcb0558049e8aca4837481f11dff',
    }

   params = urllib.parse.urlencode({
    })

   # Replace the example URL below with the URL of the image you want to analyze.
    body = "{ 'url': 'http://bradschmidt.net/wp-content/uploads/2015/04/grandpa.jpg (21kB)
' }"
    #body = open(test.jpeg).read()
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
        
       #print (python_obj[0]['scores']["anger"])
        conn.close()
    except Exception as e:
        print(e.args)

   return(bigEmotion)
