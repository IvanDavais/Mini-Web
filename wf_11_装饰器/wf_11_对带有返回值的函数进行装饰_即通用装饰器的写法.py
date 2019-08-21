"""
set_func中写的return是装饰器中的标准写法，
即使test1中没有return，这样写也照样试用，
意思是没有返回值就返回None
"""
def set_func(fn):
	def call_fn(*args, **kwargs):
		print("这是权限验证1")			
		print("这是权限验证2")
		return fn(*args, **kwargs)# 因为是这句话调动的test1函数，且test1函数存在返回值，所以这句话也需要添加return
	return call_fn

@set_func
def test1(num, *args, **kwargs):
	print("---test1---%d" %num)	
	print("---test1---", args)
	print("---test1---", kwargs)
	return "OK", "200", 300

@set_func
def test2():
	pass
 
ret = test1(100)
print(ret)

ret = test2()
print(ret)
# 此处将返回None
