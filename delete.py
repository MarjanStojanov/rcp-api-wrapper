
arg = {'status': 'active', 'created_at_min': '2019-01-01'}
print(type(arg))

url = 'https://api.rechargeapps.com/cusotomers'
data = ''

for key, value in arg:
	data = data + key + '=' + value + '&'

url = url + '?' + data
print(url)
print(data)
#result = requests.get(url, headers=self.headers)
#print(result)


'''
url2 = url + '?'
for i in list_data:
	url2 = url2 + i + '&'
	#print(url2)

print(url2)
'''
'''
bad_chars = ['\'', ')', '(', '\"']
print(arg)
data = ""
for i in range(len(arg)):
	if arg[i] in bad_chars:
		new = arg[i].strip(arg[i])
	else:
		data = str(data) + arg[i]

print(data)
'''