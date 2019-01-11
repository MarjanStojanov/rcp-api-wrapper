from objects.rest import REST
import requests, json



class Subscriptions(REST):
	
	def set_next_charge_date(self, id_, date):
		url = self.url + self.object_class + '/' + str(id_) + '/set_next_charge_date'

		#in case we don't want to pass json in data:
		data  = {"date": str(date)}
		
		result = requests.post(url, json.dumps(data), headers=self.headers)
		return result.content, result.status_code


	def cancel(self, id_, cancellation_reason):
		url = self.url + self.object_class + '/' + str(id_) + '/cancel'
	
		#in case we don't want to pass json in data:
		data  = {"cancellation_reason": str(cancellation_reason)}
	
		result = requests.post(url, json.dumps(data), headers=self.headers)
		return result.content, result.status_code


	def activate(self, id_):
		url = self.url + self.object_class + '/' + str(id_) + '/activate'

		data = {}

		result = requests.post(url, json.dumps(data), headers=self.headers)
		return result.content, result.status_code



	def delay_charge_regen(self):
		url = self.url + self.object_class + '/' + str(id_) 
	
		#in case we don't want to pass json in data:
		data  = {"commit update": False}
	
		result = requests.put(url, json.dumps(data), headers=self.headers)
		return result.content, result.status_code




"""
from rcp_wrpr import RechargeAPI as R
r = R('abc123')
r.subscription_handle.cancel(33058484, "other")
"""