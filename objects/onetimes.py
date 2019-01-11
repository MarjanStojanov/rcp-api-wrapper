from objects.rest import REST
import requests, json



class Onetimes(REST):
	
	def create(self, *args):
		data = args[0]
		url = self.url + 'addresses/' + data['address_id'] + '/' + self.object_class 

		result = requests.post(url, data=json.dumps(data), headers=self.headers)
		return result.content, result.status_code




'''
from rcp_wrpr import RechargeAPI as R
r = R('abc123')
r.charge_handle.list({"cusotmer_id": "4203912", "status": "queued"})

r.onetime_handle.create({"address_id":"25624418","next_charge_scheduled_at":"2019-12-17 00:00:00","product_title":"SuperKiwi ONETIME","price":"9","quantity":"1","shopify_variant_id":"3844892483","properties": [{"name": "grind","value": "drip"},{"name": "size","value": "medium"}]})

'''