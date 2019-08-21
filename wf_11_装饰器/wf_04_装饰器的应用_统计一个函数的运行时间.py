import time

def set_func(func):
	def call_func():
		start_time = time.time()
		func()
		stop_time = time.time()
		print("这个函数运行消耗时间：%f" %(stop_time - start_time))
	return call_func


@set_func
def test():
	print("---test---")

test()
