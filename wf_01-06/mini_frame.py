def login():
	return "------login------welcome to our website..... %s" %time.ctime()

def register():
	return "------register------welcome to our website..... %s" %time.ctime()

def profile():
	return "------profile------welcome to our website..... %s" %time.ctime()

def application(file_name):
	if file_name == "/login.py":
		return login()
	elif file_name == "/register.py":
		return register()
	elif file_name == "/profile.py":
		return profile()
	else:
		return "Not found your page..."
        
        
