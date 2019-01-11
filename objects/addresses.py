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






	
#{"address1": "3030 Nebraska Avenue","address2": "","city": "Los Angeles","province": "California","first_name": "Mike","last_name": "Flynn","zip": "90404","company": "ReCharge","phone": "3103843698","country": "United States"}
'''
from rcp_wrpr import RechargeAPI as R
r = R('abc123')
r.address_handle.count({"cusotmer_id": "22749959", "status": "2"})	
'''


#{"address1": "3030 Nebraska Avenue","state": "California","zipcode": "90404","city": "santa monica"}