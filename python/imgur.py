import imgurpython
from imgurpython import ImgurClient

imgurl = None
client_id = '41995bf67ad1bc9'
client_secret = 'f1603fce85ccb2dbbc8e6105cb26e92474b8c150'

client = ImgurClient(client_id, client_secret)

path = "../../../Jerrylogo.png"
request = client.upload_from_path(path, config=None, anon=True)

for request in request:
   imgurl = request.link 
