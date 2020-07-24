import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
import unittest
from src.models.customer import Customer
from src.models.geoLocation import GeoLocation

class TestCustomer(unittest.TestCase):
	"""
	Test cases for Geo Location model
	"""
	# Positive case
	def setUp(self):
		self.geoLocation = GeoLocation(53.339428, -6.257664)

	def test_getLatitude(self):
		self.assertEqual(self.geoLocation.getLatitude(), 53.339428)

	# Negative case
	def test_getLatitude_0(self):
		self.assertNotEqual(self.geoLocation.getLatitude(), 55)

	# Positive case
	def test_getLongitude(self):
		self.assertEqual(self.geoLocation.getLongitude(), -6.257664)

	# Negative case
	def test_getLongitude_0(self):
		self.assertNotEqual(self.geoLocation.getLongitude(), 55)

	# Positive case
	def test_getRadianLatitude(self):
		self.assertEqual(self.geoLocation.getRadianLatitude(), 0.9309486397304539)

	# Negative case
	def test_getRadianLatitude_0(self):
		self.assertNotEqual(self.geoLocation.getRadianLatitude(), 55)

	# Positive case
	def test_getRadianLongitude(self):
		self.assertEqual(self.geoLocation.getRadianLongitude(), -0.10921684028351844)

	# Negative case
	def test_getRadianLongitude_0(self):
		self.assertNotEqual(self.geoLocation.getRadianLongitude(), 55)

	# Positive case
	def test_getLocation(self):
		self.assertTrue(self.geoLocation.validDegree(90, -180, 180))

	# Negative case
	def test_getLocation_0(self):
		self.assertFalse(self.geoLocation.validDegree(180, -90, 90))

if __name__ == '__main__':
    unittest.main()

