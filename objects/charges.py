from objects.rest import REST
import requests, json



class Charges(REST):
	
	def change_next_charge_date(self, id_, date):
		url = self.url + self.object_class + '/' + str(id_) + '/change_next_charge_date'
		
		#in case we don't want to pass json in data:
		data  = {"next_charge_date": str(date)}
	
		result = requests.post(url, json.dumps(data), headers=self.headers)
		return result.content, result.status_code


	def skip(self, id_, data):
		url = self.url + self.object_class + '/' + str(id_) + '/skip'

		#in case we don't want to pass json in data:
		json_data  = {"subscription_id": str(data)}
	
		result = requests.post(url, json.dumps(json_data), headers=self.headers)
		return result.content, result.status_code


	def unskip(self, id_, data):
		url = self.url + self.object_class + '/' + str(id_) + '/unskip'

		#in case we don't want to pass json in data:
		json_data  = {"subscription_id": str(data)}
	
		result = requests.post(url, json.dumps(json_data), headers=self.headers)
		return result.content, result.status_code


	def refund(self, id_, amount):
		url = self.url + self.object_class + '/' + str(id_) + '/refund'
	
		if str(amount) == "full_refund":
			data = {"full_refund": True}
		else:
			data = {"amount": str(amount)}
	
		result = requests.post(url, json.dumps(data), headers=self.headers)
		return result.content, result.status_code




