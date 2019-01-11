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

'''
from rcp_wrpr import RechargeAPI as R
r = R('33f88f1eb3bbe75c51e265d3bb5364178e01e753b3d864a5fc195464')
r.discount_handle.remove_dicount(9668949, 25290714)	
'''