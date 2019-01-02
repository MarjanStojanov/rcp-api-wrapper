import json, requests
from objects.customer import Customers
from objects.addresses import Addresses
#from objects.addresses import Subscriptions

class RechargeAPI(object):
	def __init__(self, token):
		self.token = token
		self.customer_handle = Customers()
		self.address_handle = Addresses()
		#self.subscription_handle = Subscriptions()

	@property
	def headers(self):
		return {
			"X-Recharge-Access-Token":self.token,
			"Accept":"application/json",
			"Content-Type":"application/json",
		}

