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
        with open(const.OUTPUT_FILE_PATH, 'r') as file:
            new = file.read()

        main(self.inputFile, self.outputFile)

        with open(self.outputFile, 'r') as file:
            original = file.read()

        self.assertEqual(original, new)

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