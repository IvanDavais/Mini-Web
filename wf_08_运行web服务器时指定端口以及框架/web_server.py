import socket
import re
import threading
import time
# import dynamic.mini_frame
import sys

class WSGIServer(object):

	def __init__(self, port, app):

		# 1.创建套接字
		self.tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.tcp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		# 2.绑定
		self.tcp_socket.bind(("", port))
		# 3.变为监听套接字
		self.tcp_socket.listen(128)

		self.application = app
	

	def service_client(self,new_socket):
		request = new_socket.recv(1024).decode("utf-8")
		request_lines = request.splitlines()
		print("")
		print(">"*20)	
		# 使用正则表达式获取get /index.html http/1.1
		file_name = ""
		ret = re.match(r"[^/]+(/[^ ]*)", request_lines[0])	
		if ret:
			file_name = ret.group(1)
			print("*"*50, file_name)
			if file_name == "/":
				file_name = "/index.html"

		# 2.返回http格式的数据，给浏览器
		# 2.1 如果请求的资源不是以.py结尾，那么就认为是静态资源(http/css/js/png/jpg)

		if not file_name.endswith(".py"):
			try:	
				f = open("./static" + file_name, "rb")
			except:
				response = "HTTP/1.1 404 NOT FOUND\r\n"
				response += "\r\n"
				response += "--------file not found!------"
				new_socket.send(response.encode("utf-8"))
			else:
				html_content = f.read()
				f.close()
				# 2.返回http格式的数据，给浏览器
				response = "HTTP/1.1 200 OK\r\n"
				response += "\r\n"

				# 3.将response body发送给浏览器
				new_socket.send(response.encode("utf-8"))
				new_socket.send(html_content)

		else:
			
			# 定义一个字典作为参数传到application里
			env = dict()
			env['PATH_INFO'] = file_name

			# 调动mini_frame中的函数,传一个env字典，传一个set_response_header函数的引用
			body = self.application(env, self.set_response_header)			
			
			# 取出self_response_header运行后传入的status
			header = "HTTP/1.1 %s\r\n" %self.status
			# 取出self_response_header运行后传入的headers  
			
			for temp in self.headers:
				header += "%s:%s\r\n" %(temp[0], temp[1])

			header += "\r\n"

			response = header+body
			
			new_socket.send(response.encode("utf-8"))

		# 3.关闭套接字
		new_socket.close()

	def set_response_header(self, status, headers):
		# 接受status和header两个值
		self.status = status
		self.headers = [('server','mini_web 8.8')]
		self.headers += headers

	def runforever(self):
		
		while True:

			# 4.等待客户端的链接
			new_socket, client_addr = self.tcp_socket.accept()
			# 创建一个进程为这个客户端服务：
			p = threading.Thread(target=self.service_client, args=(new_socket,))
			p.start()


		# 6.关闭套接字
		self.tcp_socket.close()

def main():
	if len(sys.argv) == 3:
		try:
			port = int(sys.argv[1])
			frame_app_name = sys.argv[2]
		except Exception as ret:
			print("--- %s ---端口号输入有误！" %ret)
			return
	else:
		print("请输入一下格式运行此代码： ")
		print("xxx.py port")
		return

	ret = re.match(r"([^:]+):(.*)", frame_app_name)
	if ret:
		frame_name = ret.group(1) # mini_frame
		app_name = ret.group(2) # application
		print (frame_name)
		print (app_name)
	else:
		print("请输入一下格式运行此代码： ")
		print("xxx.py port")
		return

	# 给下面的import功能附加路径
	sys.path.append("./dynamic")

	# import frame_name 不行 因为import会把frame_name直接当做模块名解析，而此处的
	# frame_name不是模块名 而是变量名，这句话的结果是import会去找frame_name.py 但是
	# 文件中并没有frame_name.py

	# __import__()会去导入括号中变量所对应的值，而不是变量名本身
	# 且__import__有返回值，返回值标记着要导入的模块
	frame = __import__(frame_name)
	app = getattr(frame,app_name) #此时app就指向dynamic/mini_frame模块中的application函数

	print(app)

	wsgi_server = WSGIServer(port, app)
	wsgi_server.runforever()

if __name__ == "__main__":
	main()
