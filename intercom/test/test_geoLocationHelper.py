import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
import unittest
from src.utils.geoLocationHelper import calculateDistanceBetweenPoints
from src.models.geoLocation import GeoLocation

class TestGeoLocationHelper(unittest.TestCase):
	"""
	Test cases for Geo location helper class
	"""
	def test_calculateDistanceBetweenPoints(self):
		source = GeoLocation(53.339428, -6.257664)
		target = GeoLocation(52.986375, -6.043701)
		distance = 41.81551617632575

		dist = calculateDistanceBetweenPoints(source, target)
		self.assertEqual(dist, distance)
		self.assertIsInstance(dist, float)
		self.assertTrue(dist <= 100)
