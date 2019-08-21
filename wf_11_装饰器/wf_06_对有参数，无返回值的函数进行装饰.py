
def set_func(func):
	def call_func(a):
		print("权限检测1")
		print("权限检测2")
		# func(a) 相当于中间人，原来test1（100）直接能把100传给test1函数，现在通过func(a)传递给test1
		func(a)
	return call_func


# test1函数有参数,没有返回值
@set_func 
def test1(num):
	print("---test1---:%d" %num)

test1(100)
test1(200)
