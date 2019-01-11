from objects.rest import REST
import requests, json



class Checkouts(REST):
	
	def get_shipping_rates(self, token):
		url = self.url + self.object_class + '/' + str(token) + '/shipping_rates'

		result = requests.get(url, headers=self.headers)
		return result.content, result.status_code


	def process(self, token, data):
		url = self.url + self.object_class + '/' + str(token) + '/charge'

		result = requests.post(url, json.dumps(data), headers=self.headers)
		return result.content, result.status_code