"""
装饰按就近原则
执行按就远原则
"""
def add_qx(func):
	print("---开始装饰权限1的功能---")
	def call_func(*args, **kwargs):
		print("---权限11111---")
		return func(*args, **kwargs)
	return call_func

def add_xx(func):
	print("---开始装饰权限2的功能---")
	def call_func(*args, **kwargs):
		print("---权限22222---")
		return func(*args, **kwargs)
	return call_func


def add_yy(func):
	print("---开始装饰权限3的功能---")
	def call_func(*args, **kwargs):
		print("---权限33333---")
		return func(*args, **kwargs)
	return call_func

# 代码执行到@add_qx这行准备装饰的时候发现下面是一个装饰器add_xx，而不是函数，所以它就先让下一行首先进行装饰
# 等下面的@add_xx进行装饰完成就变成了一个函数，于是上一行的@add_qx就可以就行装饰了 

@add_qx
@add_xx #等价于test1 = add_xx(test1)
@add_yy
def test1():
	print("---test1---")

test1()

