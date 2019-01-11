from objects.rest import REST
import requests, json



class Orders(REST):

	def change_order_date(self, id_, date):
		url = self.url + self.object_class + '/' + str(id_) + '/change_date'
	
		#in case we don't want to pass json in data:
		data  = {"scheduled_at": str(date)}
		
		result = requests.post(url, json.dumps(data), headers=self.headers)
		return result.content, result.status_code


	def change_order_varinat(self, id_, old_variant_id, new_variant_id):
		url = self.url + self.object_class + '/update_shopify_variant' + variant_id

		#in case we don't want to pass json in data:
		data  = {"shopify_variant_id": str(old_variant_id), "new_shopify_variant_id": str(new_variant_id)}
		
		result = requests.post(url, json.dumps(data), headers=self.headers)
		return result.content, result.status_code


	def clone_order(self, id_, charge_id, date):
		url = self.url + self.object_class + '/clone_order_on_success_charge/' + str(id_) + '/charge/' + str(charge_id)
		print(date)
		#in case we don't want to pass json in data:
		data  = {"scheduled_at": str(date)}
		print(json.dumps(data))
		result = requests.post(url, json.dumps(data), headers=self.headers)
		return result.content, result.status_code


'''
from rcp_wrpr import RechargeAPI as R
r = R('abc123')
r.order_handle.clone_order(70071201,97376832, 2022-11-16)
'''