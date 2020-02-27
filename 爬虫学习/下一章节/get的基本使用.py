import urllib.request
import urllib.parse
print("请输入您想搜的内容：")
word=input()
url='https://www.baidu.com/s?'
data={
	'ie':'utf-8',
	'wd':word,
}
quety_string=urllib.parse.urlencode(data)
url+=quety_string
reaponse=urllib.request.urlopen(url)
filename=word+".html"
with open(filename,'wb')as fp:
	fp.write(reaponse.read())
