import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
import unittest
from src.models.customer import Customer
from src.models.geoLocation import GeoLocation
from src.service.customerService import CustomerService
import src.constants.constant as const

class TestCustomerService(unittest.TestCase):
	"""
	Test cases for Customer Service
	"""
	totalCustomers = 32
	invitedCustomer = 16
	intercomLocation = GeoLocation(53.339428, -6.257664)
	maxDistance = 100

	def test_getCustomers(self):
		customers = CustomerService.getCustomers(const.CUSTOMER_FILE_PATH)
		self.assertTrue(customers != None);
		self.assertIsInstance(customers, list)
		self.assertEqual(len(customers), self.totalCustomers)

	def test_filterCustomers(self):
		customers = CustomerService.getCustomers(const.CUSTOMER_FILE_PATH)
		customerList = CustomerService.filterCustomers(customers, self.intercomLocation, self.maxDistance)
		self.assertTrue(customerList != None);
		self.assertIsInstance(customerList, list)
		self.assertEqual(len(customerList), self.invitedCustomer)

	def test_calculateDistance(self):
		invited = CustomerService.calculateDistance(Customer(1, "Mark", 53.2451022, -6.238335), self.intercomLocation, self.maxDistance)
		self.assertTrue(invited);
		self.assertIsInstance(invited, bool)

	# Negative test
	def test_calculateDistance_0(self):
		invited = CustomerService.calculateDistance(Customer(1, "Alice", 51.92893, -10.27699), self.intercomLocation, self.maxDistance)
		self.assertFalse(invited);
		self.assertIsInstance(invited, bool)

	def test_buildOutputFile(self):
		customers = CustomerService.getCustomers(const.CUSTOMER_FILE_PATH)
		output = CustomerService.buildOutputFile(customers, self.totalCustomers, const.OUTPUT_FILE_PATH)
		self.assertTrue(output != None);
		self.assertIsInstance(output, str)