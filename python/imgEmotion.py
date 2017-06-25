import http.client, urllib.request, urllib.parse, urllib.error, base64, sys, json
import feed as feed
headers = {
 # Request headers. Replace the placeholder key below with your subscription key.
    'Content-Type': 'application/octet-stream',
    'Ocp-Apim-Subscription-Key': ' 6064bcb0558049e8aca4837481f11dff',
    }

params = urllib.parse.urlencode({
     })

 # Replace the example URL below with the URL of the image you want to analyze.
 # body = open(../Lib/Screencaps/*.jpeg).read()
# body = open(feed.imgpath).read()
try:
    # NOTE: You must use the same region in your REST call as you used to obtain your subscription keys.
    #   For example, if you obtained your subscription keys from westcentralus, replace "westus" in the 
    #   URL below with "westcentralus".
    conn = http.client.HTTPSConnection('westus.api.cognitive.microsoft.com')
    conn.request("POST", "/emotion/v1.0/recognize?%s" % params, body, headers)

    response = conn.getresponse()
    data = response.read()
    python_obj = json.loads(data)
    print (python_obj[0]['scores'])
    print(data)
    conn.close()
except Exception as e:
     print(e.args)
 ####################################

emotion = None
emojicode = None
#Replace with Azure variables
if  emotion == "Happy":
    emojicode == u"U+1F603" 
elif emotion == "Sad":
    emojicode == u"U1F61E",  
elif emotion == "Confused":
    emojicode == u"U+1F616",  
elif emotion == "Calm":
    emojicode == u"U+1F60C",  
elif emotion == "Angry":
    emojicode == u"U+1F621",  
elif emotion == "Suprised":
    emojicode == u"U+1F602",  
