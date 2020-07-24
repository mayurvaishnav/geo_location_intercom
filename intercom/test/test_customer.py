import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
import unittest
from src.models.customer import Customer
from src.models.geoLocation import GeoLocation

class TestCustomer(unittest.TestCase):
	"""
	Test cases for Customer model
	"""
	def setUp(self):
		self.customer = Customer(1, "Christina", 52.986375, -6.043701)

	# Positive case
	def test_getUserId(self):
		self.assertEqual(self.customer.getUserId(), 1)

	# Negative case
	def test_getUserId_0(self):
		self.assertNotEqual(self.customer.getUserId(), 2)

	# Positive case
	def test_getName(self):
		self.assertEqual(self.customer.getName(), "Christina")

	# Negative case
	def test_getName_0(self):
		self.assertNotEqual(self.customer.getName(), "Martha")

	# Positive case
	def test_getLatitude(self):
		self.assertEqual(self.customer.getLatitude(), 52.986375)

	# Negative case
	def test_getLatitude_0(self):
		self.assertNotEqual(self.customer.getLatitude(), 55)

	# Positive case
	def test_getLongitude(self):
		self.assertEqual(self.customer.getLongitude(), -6.043701)

	# Negative case
	def test_getLongitude_0(self):
		self.assertNotEqual(self.customer.getLongitude(), 55)

	# Positive case
	def test_getLocation(self):
		self.assertIsInstance(self.customer.getLocation(), GeoLocation)

if __name__ == '__main__':
    unittest.main()

