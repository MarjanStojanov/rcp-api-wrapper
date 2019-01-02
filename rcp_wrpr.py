import json, requests

class RechargeAPI(object):
	def __init__(self, token):
		self.token = token
		self.headers = {
			"X-Recharge-Access-Token":token,
			"Accept":"application/json",
			"Content-Type":"application/json",
		}
		self.url = 'https://api.rechargeapps.com/' + self.__class__.__name__.lower() + 's' if self.__class__.__name__ != 'RechargeAPI' else '' 
