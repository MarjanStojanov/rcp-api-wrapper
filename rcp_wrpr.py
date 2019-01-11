from objects.customers import Customers
from objects.addresses import Addresses
from objects.subscriptions import Subscriptions
from objects.charges import Charges
from objects.orders import Orders
from objects.onetimes import Onetimes
from objects.checkouts import Checkouts
from objects.discounts import Discounts
from objects.webhooks import Webhooks
from objects.metafields import Metafields
from objects.collections import Collections
from objects.products import Products
from objects.rest import REST



from objects.rest import REST


class RechargeAPI(object):
	def __init__(self, token):
		REST.token = token
		self.cusotmer = Customers()
		self.address = Addresses()
		self.subscription = Subscriptions()
		self.charge = Charges()
		self.order = Orders()
		self.onetime = Onetimes()
		self.checkout = Checkouts()
		self.discount = Discounts()
		self.webhook = Webhooks()
		self.metafield = Metafields()
		self.collection = Collections()
		self.product = Products()
