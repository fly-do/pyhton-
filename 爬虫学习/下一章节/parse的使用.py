import urllib.parse
name='http://www.baidu'
name1="老牛"
age=18
list={
	'name':name1,
	'age':age,
}
it=[]
for k,v in list.items():
	it.append(k+'='+str(v))
quety_string='&'.join(it)
name100=name+'?'+quety_string
print(name100)
'''
第二种方法：
'''
quety_string1=urllib.parse.urlencode(list)
a=name+quety_string1
print(a)