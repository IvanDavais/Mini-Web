# 只要系统碰到@set——func就开始执行

def set_func(func):
	print("---开始装饰---")
	def call_func(a):
		print("权限验证1")
		print("权限验证2")
		func(a)
	return call_func

@set_func
def test1(num):
	print("---test1--- %d" %num) 

