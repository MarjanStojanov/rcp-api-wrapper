def query_builder(arg):
		data = ''
		for key, value in arg.items():
			data = data + key + '=' + value + '&'

		return data