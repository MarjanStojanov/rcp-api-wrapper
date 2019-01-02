class REST:
	def update(self):
		print('Updated: ' + self.__class__.__name__)

	def create(self):
		print('Created: ' + self.__class__.__name__)

	def delete(self):
		print('Deleted: ' + self.__class__.__name__)

	def count(self):
		print(self.__class__.__name__ + ' count: ')

	def list(self, JSON):
		pass
