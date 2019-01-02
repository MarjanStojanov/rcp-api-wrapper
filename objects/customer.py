from rcp_wrpr import RechargeAPI

import requests, json

class Customer(RechargeAPI):
	def __init__(self):
		self.name='marjan'
	def printy(self):
		print json.dumps(self.__dict__, indent=4)

	def update(self, id_, JSON):
		result = requests.put(self.url + '/' + str(id_), headers=self.headers, data=json.dumps({}))
		print(result.status_code)
		print(result.json())
