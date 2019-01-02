from objects.customers import Customers
from objects.addresses import Addresses
from objects.subscriptions import Subscriptions
from objects.charges import Charges
from objects.orders import Orders
from objects.discounts import Discounts
from objects.webhooks import Webhooks
from objects.checkouts import Checkouts
from objects.metafields import Metafields
from objects.onetimes import Onetimes



class RechargeAPI(object):
	def __init__(self, token):
		self.token = token
		self.customer_handle = Customers()
		self.address_handle = Addresses()
		self.subscription_handle = Subscriptions()
		self.charge_handle = Charges()
		self.order_handle = Orders()
		self.discount_handle = Discounts()
		self.webhook_handle = Webhooks()
		self.checkout_handle = Checkouts()
		self.metafield_handle = Metafields()
		self.onetime_handle = Onetimes()


	@property
	def headers(self):
		return {
			"X-Recharge-Access-Token":self.token,
			"Accept":"application/json",
			"Content-Type":"application/json",
		}
