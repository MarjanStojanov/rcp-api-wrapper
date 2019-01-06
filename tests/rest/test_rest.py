import sys
sys.path.insert(0, '../..')

import objects
from rcp_wrpr import RechargeAPI
from unittest import TestCase


class TestRest(TestCase):
	def setUp(self):
		self.api1 = RechargeAPI('token')

	def tearDown(self):
		pass

	def test_calling_with_various_handles(self):	
		assert self.api1.customer_handle.object_class == 'customers'
		assert self.api1.address_handle.object_class == 'addresses'
		assert self.api1.subscription_handle.object_class == 'subscriptions'
		assert self.api1.charge_handle.object_class == 'charges'
		assert self.api1.order_handle.object_class == 'orders'
		assert self.api1.discount_handle.object_class == 'discounts'
		assert self.api1.webhook_handle.object_class == 'webhooks'
		assert self.api1.metafield_handle.object_class == 'metafields'
		assert self.api1.checkout_handle.object_class == 'checkouts'
		assert self.api1.onetime_handle.object_class == 'onetimes'

	def test_valid_headers(self):
		headers = {
			'X-Recharge-Access-Token':self.api1.token,
			'Content-Type':'application/json',
			'Accept':'application/json',
		}

		self.assertEqual(self.api1.customer_handle.headers, headers)

	def test_delete(self):
		pass

	def test_count(self):
		pass

	def test_list(self):
		pass
 