from objects.rest import REST 
import requests, json
from objects.helpers import query_builder



class Addresses(REST):

	def create(self, customer_id, data):

		url = self.url + 'customers/' + str(customer_id) + '/' + self.object_class
		print(url)
		result = requests.post(url, json.dumps(data), headers=self.headers)
		return result.content, result.status_code


	def list(self, *arg):
				
		if "cusotmer_id" in arg[0]:
			print("first")
			url = self.url + 'customers/' + arg[0]['cusotmer_id'] + '/addresses'		
			
			result = requests.get(url, headers=self.headers)
			return result.content, result.status_code

			if result.status_code == 404:
				response = {"error": "you can search only by customer_id"}
				return response, result.status_code

		else:
			data = query_builder(arg[0])
			url = self.url + self.object_class + '?' + data
			result = requests.get(url, headers=self.headers)
			return result.content, result.status_code


	def validate(self, data):
		url = url = self.url + self.object_class + '/validate'
		result = requests.post(url, data=json.dumps(data), headers=self.headers)
		return result.content, result.status_code





