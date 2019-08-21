"""
为什么这个版本不合理呢，因为在权限验证的时候不可能是由被验证方自己输入验证级别
"""
def set_func(func):
	def call_func(*args, **kwargs):
		level = args[0]
		if level == 1:
			print("---权限级别1，验证---")
		elif level == 2:
			print("---权限级别2，验证---")
		return func()
	return call_func

@set_func
def test1():
	print("---test1---")
	return "OK"

@set_func
def test2():
	print("---test2---")
	return "OK"

# 自己输入验证级别
test1(1)
test1(2)



