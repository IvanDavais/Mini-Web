def set_level(level):
	def set_func(func):
		def call_func(*args, **kwargs):
			if level == 1:
				print("---权限级别1，验证---")
			elif level == 2:
				print("---权限级别2，验证---")
			return func()
		return call_func
	return set_func


# 1.调用set_func并且将1当做实参传递
# 2.用上一步调用的返回值当做装饰器对test1函数进行装
@set_level(1)
def test1():
	print("---test1---")
	return "OK"

@set_level(2)
def test2():
	print("---test2---")
	return "OK"

# 自己输入验证级别
test1()
test2()
