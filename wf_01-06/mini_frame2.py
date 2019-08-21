def index():
	return "This is home page"
def login():
	return "This is login page"
def register():
	return "This is register page"	

def application(environ, start_response):
	start_response('200 OK', [('Content_Type', 'text/html;charset=utf-8')])
	file_name = environ['PATH_INFO']

	if file_name == "/index.py":
		return index()

	elif file_name == "/login.py":
		return login()

	elif file_name == "/register.py":
		return register()

	else:
		return "NOT FOUND!"
