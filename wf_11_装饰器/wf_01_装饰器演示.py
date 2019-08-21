# 注意：这个函数需要传参
def set_func(func):
	def call_fun():
		print("权限验证1")
		print("权限验证2")
		func()
	return call_fun

@set_func
def test1():
	print("---test1---")

test1()
