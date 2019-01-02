from rest import REST 
import requests, json

class Addresses(REST):
	
	def validate(self):
		print('Validating: '+self.__class__.__name__)
