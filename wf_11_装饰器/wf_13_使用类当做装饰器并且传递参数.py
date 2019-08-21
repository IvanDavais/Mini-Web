class Test(object):
	def __init__(self, func):
		self.func = func
	
	def __call__(self, *args, **kwargs):
		print("这里是装饰器的call方法")
		self.func(*args, **kwargs)
	



@Test
def get_str(num, *args, **kwargs):
	print("---0---%d" %num)
	print("---1---", args )
	print("---2---", kwargs)


get_str(1, 2, name:"FanWan")
 
