from time import ctime, sleep

def timefun_args(pre="hello"):
	def timefun(func):
		def wrapped_func():
			print("%s called at %s from %s" %(func.__name__, ctime(), pre))
			return func()
		return wrapped_func
	return timefun

@timefun_args("python")
def foo():
	print("I am foo")
	
@timefun_args("itcatst")
def too():
	print("I am too")

foo()
sleep(3)
too()
