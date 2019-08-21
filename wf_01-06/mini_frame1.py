def application(environ, start_response):
	start_response('200 OK', [('Content_Type', 'text/html;charset=utf-8')])
	return "I love you Chian 我..."
