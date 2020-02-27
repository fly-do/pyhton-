print("hello,world!")
import urllib.request
url="http://www.baidu.com"
a=urllib.request.urlopen(url=url)
#print(a.read().decode())
with open('baidu.html','w',encoding='utf8')as fp:
    fp.write(a.read().decode())
print(a.geturl())
print(a.getheaders())
print(dict(a.getheaders()))
print(a.getcode())
print(a.readlines())