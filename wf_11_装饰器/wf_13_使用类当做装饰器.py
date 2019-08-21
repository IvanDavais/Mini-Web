class Test(object):
	def __init__(self, func):
		self.func = func
	
	def __call__(self):
		print("这里是装饰器的call方法")
		return self.func()	



@Test
def get_str():
	return "haha"

print(get_str()) 
