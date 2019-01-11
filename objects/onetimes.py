from objects.rest import REST
import requests, json



class Onetimes(REST):
	
	def create(self, *args):
		data = args[0]
		url = self.url + 'addresses/' + data['address_id'] + '/' + self.object_class 

		result = requests.post(url, data=json.dumps(data), headers=self.headers)
		return result.content, result.status_code



