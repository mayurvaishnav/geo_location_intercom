import src.constants.constant as const
import src.models.customer as cust
from src.utils.geoLocationHelper import calculateDistanceBetweenPoints
from src.utils.fileIOHelper import writeIntoFile, readFile
import json

class CustomerService(object):
    """
    Controller for clustomers.
    """
    
    @staticmethod
    def getCustomers(filePath):
        """
        Reads input file, parses the json and returns all the customer data built from the input file

        Parameters:
            filePath (str): path of the input file

        Returns:
            (List): list of the customer objects
        """
        try:
            fileData = readFile(filePath)

            if fileData is None:
                return None
            return list(map(lambda line:cust.Customer(**json.loads(line.strip())), fileData))
        except (ValueError) as e:
            print('Input file provided is not in json format. Error: ', e)
            return None
        except (Exception) as e:
            print(e)
            return None

    @staticmethod
    def filterCustomers(customers, intercomLocation, maxDistance):
        """
        Filter customers who are within given maximum distance

        Parameters:
            customers (List): list of customers objects
            intercomLocation (GeoLocation): an object of GeoLocation
            maxDistance (int): maximum distance in KM

        Returns:
            (List): list of the filtered customer objects who are within given distance
        """
        return sorted(list(filter(lambda customer: CustomerService.calculateDistance(customer, intercomLocation, maxDistance), customers)), key=lambda key: key.getUserId())
        # sorted(ut, key=lambda x: x.count, reverse=True)
    
    @staticmethod
    def calculateDistance(customer, intercomLocation, maxDistance):
        """
        Check whether the customer is within the given distance.

        Parameters:
            customer (Customer): an object of Customer
            intercomLocation (GeoLocation): an object of GeoLocation
            maxDistance (int): maximum distance in KM

        Returns:
            (Boolean): True if the customer is within given distance else False
        """
        try:
            print("Calculating Distance for ", customer.getUserId(), end = '');
            
            distance = calculateDistanceBetweenPoints(customer.getLocation(), intercomLocation);
            filterCustomer = distance <= maxDistance;
            
            if(filterCustomer):
                print(" - ", distance , " - Within Distance");
            else:
                print(" - ", distance , " - Not within Distance");
            
            return filterCustomer;
            
        except (Exception) as e:
            print(e);
            return False

    def buildOutputFile(customers, totalCustomerCount, path):
        """
        Create the output string.

        Parameters:
            customer (Customer): an object of filtered Customer
            totalCustomerCount (int): total customers in the input file 
            path (str): path of the output file

        Returns:
            (str): path if the output file
        """
        string = "Total Customers: " + str(totalCustomerCount)
        string += "\nCustomer within " + str(const.MAX_DISTANCE_KM) + " KM: " + str(len(customers))
        string += "\n\n"

        for customer in customers:
            string += str(customer.getUserId()) + "  " + str(customer.getName()) + "  \n"
        
        try:
            return writeIntoFile(string, path)
        except Exception as e:
            print(e)
            return  None