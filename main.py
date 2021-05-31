import urllib.request as req
import json

url = 'http://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&nc=1614319565639&pid=hp&FORM=BEHPTB&uhd=1&uhdwidth=3840&uhdheight=2160'

# try:
res = req.urlopen(url)
res = res.read().decode('utf-8')

api = json.loads(res)

api = api['images']
downloadURL = "https://bing.com" + api[0]['url']
dateTime = api[0]['startdate']

req.urlretrieve(downloadURL, './wallpaper/{}.jpg'.format(dateTime))

# except:
#     print("Error.")
    