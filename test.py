import urllib.request as req
    
url = "https://cdn.jsdelivr.net/gh/oCoke/cdn@master/avatar/yfun.min.jpeg"
req.urlretrieve(url, 'yfun.jpg')