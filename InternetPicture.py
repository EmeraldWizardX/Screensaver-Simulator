import shutil
import requests

#image URL
class internetPic:
    def __init__(self,url):
        self.url=url
    def getpic(self):

        #open url,stream is true, this returns stream content
        image = requests.get(self.url,stream=True)
        #open local file for tempt image(Wtrit binary)
        local_file=open("BaseImage.png", "wb")
        #set decode to true because if not the size will be 0
        image.raw.decode_content=True

        #copy new image to local image
        shutil.copyfileobj(image.raw,local_file)

        #delete url
        del image