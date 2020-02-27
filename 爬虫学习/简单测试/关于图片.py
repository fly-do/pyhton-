import urllib.request
url='http://img.juimg.com/tuku/yulantu/120331/2445-12033109125535.jpg'
a=urllib.request.urlopen(url)
with open('caoyuan.jpg','wb')as fp:
    fp.write(a.read())
#另一种方法：
urllib.request.urlretrieve(url,'草原.jpg')
