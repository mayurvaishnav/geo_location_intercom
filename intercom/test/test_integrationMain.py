import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
import unittest
from unittest.mock import patch, Mock
from src.models.geoLocation import GeoLocation
from src.service.customerService import CustomerService
from src.models.customer import Customer
import src.constants.constant as const
from main import main

class TestIntegrationMain(unittest.TestCase):
    """
    Integration test cases as whole system
    """ 
    totalCustomers = 32
    invitedCustomer = 16
    intercomLocation = GeoLocation(53.339428, -6.257664)
    maxDistance = 100
    inputFile = path.join(const.ROOT_DIR, 'test_customers.txt')
    outputFile = path.join(const.ROOT_DIR, 'output/test_output.txt')

    def test_main(self):
        originalOutputFile = 'Total Customers: 32\n'
        originalOutputFile += 'Customer within 100 KM: 16\n\n'
        originalOutputFile += '"user_id": 4, "name: " Ian Kehoe, "latitude: " 53.2451022, "longitude: " -6.238335\n'
        originalOutputFile += '"user_id": 5, "name: " Nora Dempsey, "latitude: " 53.1302756, "longitude: " -6.2397222\n'
        originalOutputFile += '"user_id": 6, "name: " Theresa Enright, "latitude: " 53.1229599, "longitude: " -6.2705202\n'
        originalOutputFile += '"user_id": 8, "name: " Eoin Ahearn, "latitude: " 54.0894797, "longitude: " -6.18671\n'
        originalOutputFile += '"user_id": 11, "name: " Richard Finnegan, "latitude: " 53.008769, "longitude: " -6.1056711\n'
        originalOutputFile += '"user_id": 12, "name: " Christina McArdle, "latitude: " 52.986375, "longitude: " -6.043701\n'
        originalOutputFile += '"user_id": 13, "name: " Olive Ahearn, "latitude: " 53, "longitude: " -7\n'
        originalOutputFile += '"user_id": 15, "name: " Michael Ahearn, "latitude: " 52.966, "longitude: " -6.463\n'
        originalOutputFile += '"user_id": 17, "name: " Patricia Cahill, "latitude: " 54.180238, "longitude: " -5.920898\n'
        originalOutputFile += '"user_id": 23, "name: " Eoin Gallagher, "latitude: " 54.080556, "longitude: " -6.361944\n'
        originalOutputFile += '"user_id": 24, "name: " Rose Enright, "latitude: " 54.133333, "longitude: " -6.433333\n'
        originalOutputFile += '"user_id": 26, "name: " Stephen McArdle, "latitude: " 53.038056, "longitude: " -7.653889\n'
        originalOutputFile += '"user_id": 29, "name: " Oliver Ahearn, "latitude: " 53.74452, "longitude: " -7.11167\n'
        originalOutputFile += '"user_id": 30, "name: " Nick Enright, "latitude: " 53.761389, "longitude: " -7.2875\n'
        originalOutputFile += '"user_id": 31, "name: " Alan Behan, "latitude: " 53.1489345, "longitude: " -6.8422408\n'
        originalOutputFile += '"user_id": 39, "name: " Lisa Ahearn, "latitude: " 53.0033946, "longitude: " -6.3877505\n'

        print(originalOutputFile)

        main(self.inputFile, self.outputFile)

        with open(self.outputFile, 'r') as file:
            testOutputFile = file.read()

        self.assertEqual(originalOutputFile, testOutputFile)

    # @patch(CustomerService.getCustomers, return_value = [Customer(1, "Christina", 52.986375, -6.043701)])
    # @patch(CustomerService)
    # def test_getCustomerMock(self):
    #     customerService = Mock()

    #     customerService.getCustomers.return_value = [
    #         Customer(1, "Christina", 52.986375, -6.043701)
    #     ]

    #     response = customerService.getCustomers(self.inputFile)
    #     self.assertIsNotNone(response)
    #     self.assertIsInstance(response, list)
    #     self.assertIsInstance(response[0], Customer)