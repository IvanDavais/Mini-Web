
x = 300

def test1():
	x =200
	def test2():
		# 注意：修改闭包外部的变量时使用nonlocal，而不是global 且python2中无法使用
		nonlocal x
		print("---1--- x=%d" %x)
		x = 100 # 此时x修改的是x=200 这个x，因为前面已经加了nonlocal x
		print("---2--- x=%d" %x)

	return test2

t1 = test1()
t1()

