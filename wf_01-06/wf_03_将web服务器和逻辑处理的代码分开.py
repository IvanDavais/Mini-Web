import socket
import re
import threading
import time
import mini_frame

class WSGIServer(object):

	def __init__(self):

		# 1.创建套接字
		self.tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.tcp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		# 2.绑定
		self.tcp_socket.bind(("", 7890))
		# 3.变为监听套接字
		self.tcp_socket.listen(128)
	

	def service_client(self,new_socket):
		request = new_socket.recv(1024).decode("utf-8")
		request_lines = request.splitlines()
		print("")
		print(">"*20)
		print(request_lines)

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
				f = open("./html" + file_name, "rb")
			except:
				response = "http/1.1 404 not found\r\n"
				response += "\r\n"
				response += "--------file not found!"
				new_socket.send(response.encode("utf-8"))
			else:
				html_content = f.read()
				f.close()

				# 2.返回http格式的数据，给浏览器
				response = "http/1.1 200 ok\r\n"
				response += "\r\n"

				# 3.将response body发送给浏览器
				new_socket.send(response.encode("utf-8"))
				new_socket.send(html_content)

		else:
			# 如果是.Py结尾的就认为是动态资源请求
			header = "HTTP/1.1 200 OK\r\n"
			header += "\r\n"
			
			# 此处调用mini_frame中的函数	
			# body ="see time:%s" %time.ctime()	
			body = mini_frame.login()			

			response = header+body
			
			new_socket.send(response.encode("utf-8"))

		# 3.关闭套接字
		new_socket.close()


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
	wsgi_server = WSGIServer()
	wsgi_server.runforever()

if __name__ == "__main__":
	main()
