class REST:
	def __init__(self):
		self.object_class = self.__class__.__name__.lower()
		self.url = 'https://api.rechargeapps.com/' + self.object_class + '/'

	@property
	def headers(self):
		return {
			"X-Recharge-Access-Token":self.token,
			"Accept":"application/json",
			"Content-Type":"application/json",
		}

	def update(self, id):
		print('Updated: ' + self.url)

	def create(self, id):
		print('Created: ')

	def delete(self, id):
		print('Deleted: ')

	def count(self):
		print(' count: ')

	def list(self, JSON):
		pass
