from time import ctime, sleep

def timefun(func):
	def wrapped_func():
		print("%s called at %s" %(func.__name__, ctime()))
		# 此处需要加上return，如果不加，则在执行getInfo时会返回None，而不是"---I am getInfo---"
		return func()
	return wrapped_func

@timefun
def foo():
	print("I am foo")

@timefun
def getInfo():
	return "---I am getInfo---"

foo()
sleep(3)
print(getInfo())

