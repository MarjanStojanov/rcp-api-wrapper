from objects.rest import REST
import requests, json


class Webhooks(REST):

	def validate(self, id_):
		url = self.url + self.object_class + '/' + str(id_) + '/test'
		
		result = requests.post(url, data=json.dumps({}), headers=self.headers)
		return result.content, result.status_code

