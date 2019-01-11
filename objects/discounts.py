from objects.rest import REST
import requests, json



class Discounts(REST):

	def add_discount_to_address(self, address_id, code):
		url = self.url + 'addresses/' + str(address_id) + '/discounts/' + code + '/apply'

		result = requests.post(url, data=json.dumps(data), headers=self.headers)
		return result.content, result.status_code


	def add_discount_to_charge(self, charge_id, code):
		url = self.url + 'charges/' + str(charge_id) + '/discounts/' + code + '/apply'

		result = requests.post(url, data=json.dumps(data), headers=self.headers)
		return result.content, result.status_code


	def remove_dicount(self, id_, data):
		url = self.url + self.object_class + '/' + str(id_) + '/remove'
		data = {"address_id":str(data)}

		result = requests.put(url, data=json.dumps(data), headers=self.headers)
		return result.content, result.status_code
