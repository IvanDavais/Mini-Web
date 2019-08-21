"""
装饰器的作用是：在不改变原函数的情况下，做到对原函数功能的扩展
"""

def set_func(func):
	def call_func():
		print("权限检测1")
		print("权限检测2")
		func()
	return call_func


@set_func  # 等价于test1 = set_func(test1)
def test1():
	print("---test1---")



# 过渡版本
# ret = set_fun(test1)
# ret()

# 此处先执行set_func(test1) 然后再将这个值赋予给test1，所以跟上面的过渡版本没差别
# 且这么写的优势在于往下所有需要调用test1方法的地方无需改名使用ret，这样就不要大规模修改代码
# test1 = set_func(test1)



test1()
