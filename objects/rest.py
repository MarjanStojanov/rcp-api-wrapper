import requests, json
from objects.helpers import query_builder


class REST:
	token = None
	
	def __init__(self):
		self.object_class = self.__class__.__name__.lower()
		self.url = 'https://api.rechargeapps.com/' 

	@property
	def headers(self):
		return {
			"X-Recharge-Access-Token":REST.token,
			"Accept":"application/json",
			"Content-Type":"application/json",
		}

	def create(self, data):
		url = self.url + self.object_class + '/'
		result = requests.post(url, json.dumps(data), headers=self.headers)
		return result.content, result.status_code


	def update(self, id_, data):
		url = self.url + self.object_class + '/'+ str(id_)
		result = requests.put(url, json.dumps(data), headers=self.headers)	
		return result.content, result.status_code


	def retrieve(self, id_):
		url = self.url + self.object_class + '/' + str(id_)
		result = requests.get(url, headers=self.headers)
		return result.content, result.status_code


	def delete(self, id_):
		url = self.url + self.object_class + '/' + str(id_)
		result = requests.request("DELETE", url, headers=self.headers)
		return result.content, result.status_code


	def list(self, *arg):	
		
		if arg != ():
			data = query_builder(arg[0])
			url = self.url + self.object_class + '?' + data
		
		else:
			url = self.url + self.object_class + '?' 
		
		result = requests.get(url, headers=self.headers)
		return result.content, result.status_code


	def count(self, *arg):
		url = self.url + self.object_class + '/count?'
		if arg:
			data = query_builder(arg[0])
			url = self.url + self.object_class + '/count?' + data
		 
		result = requests.get(url, headers=self.headers)
		return result.content, result.status_code



	


