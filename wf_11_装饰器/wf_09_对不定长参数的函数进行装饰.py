def set_func(func):
	def call_func(*args, **kwargs):
		print("权限验证1")
		print("权限验证2")
		#func(args, kwargs) # 这样写不行，相当于传递了2个参数：1个元组，一个字典，
		func(*args, **kwargs) # 拆包
	return call_func

@set_func
def test1(num, *args, **kwargs):
	print("---test1---%d" %num)
	print("---test1---", args)
	print("---test1---", kwargs)

test1(100)
test1(100, 200)
test1(100, 200, 300, name="FanWan")
