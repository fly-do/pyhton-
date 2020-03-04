'''
目录：
	求绝对值：17				随机数：73
	true与false的运算：21		开平方：70
	取n个数中的最大值：38		向下取整：60
	取n个数中的最小值：44		1返回整数部分与小数部分：67
	求x的y次方：47				指定范围的值：80
	四舍五入的方法：50			随机生成一个包含0，但不包含1的数：87
	向上取整：57				列表随机排序：90
	随机生产一个实数：95
	
	
	
'''
import math	
import random		
		# 求绝对值：
a1 = -10
print(abs(a1))

		# true与false的运算：
print((6 > 9) - (6 < 9))
	# false - true = -1

print((6 < 9) - (6 > 9))
	# ture - false = 1
	
print((6 > 9) + (6 < 9))
	# false + true = 1

print((6 < 9) + (6 > 9))
	# ture + false = 1
'''
	true = 1
	false = 0
'''

		# 取n个数中的最大值：
a2 = 7
a3 = 100
a4 = 40
print(max(a2, a3,a4))

		# 取n个数中的最小值：
print(min(a2, a3,a4))

		# 求x的y次方：
print(pow(4,5))

		# 四舍五入的方法：
print(round(3.274,2))
'''
	逗号前是输入你想约算的数值
	都好后面是你想精确到的位数
'''

		# 向上取整：
print(math.ceil(15.7))
print(math.ceil(15.1))
# 都是16

		# 向下取整：
print(math.floor(15.7))
print(math.floor(15.1))
# 都是15

		# 返回整数部分与小数部分：
print(math.modf(22.3))

		# 开平方：
print(math.sqrt(123123))

		# 随机数：
print(random.choice([1,3,7,9]))
# 需要倒random包
# 也可以是一个字符串
print(random.choice(range(5)))
# 会生成一个0-4之间一个数

# 指定范围的开始值：
print(random.randrange(1,100,2))
'''
	"1"是指定范围的开始值，包含在范围内。
	"100"是指定范围的结束值，不包含在范围内。
'''

# 随机生成一个包含0，但不包含1的数：
print(random.random())

# 列表随机排序：
list = [1,2,3,4,5]
random.shuffle(list)
print(list)

# 随机生产一个实数：
print(random.uniform(3,9))
# 他在3~9范围内




