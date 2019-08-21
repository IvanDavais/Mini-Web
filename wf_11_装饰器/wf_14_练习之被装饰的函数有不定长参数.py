from time import ctime, sleep

def timefun(func):
	def wrapped_func(*args, **kwargs):
		print("%s called at %s" %(func.__name__, ctime()))
		print(*args, **kwargs)
		func(*args,**kwargs)
	return wrapped_func	

@timefun	
def foo(a, b, c):
	print(a + b + c)

foo(1,2,3)
sleep(3)
foo(4,5,6)

