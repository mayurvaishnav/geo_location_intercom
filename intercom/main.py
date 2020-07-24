import src.constants.constant as const
import src.models.geoLocation as geoLocation
from src.service.customerService import CustomerService

def main(inputFile, outputFile):
    """
    Main function which call all the necessary functions.
    """
    customers = CustomerService.getCustomers(inputFile)

    if customers is None:
        print("No customer found!")
        return

    intercomLocation = geoLocation.GeoLocation(const.INTERCOM_OFFICE_LATITUDE, const.INTERCOM_OFFICE_LONGITUDE)

    customerList = CustomerService.filterCustomers(customers, intercomLocation, const.MAX_DISTANCE_KM)

    outputFilePath = CustomerService.buildOutputFile(customerList, len(customers), outputFile)

    if outputFilePath is None:
        print("Cannot write into file")
        return
    
    print("Output file created at ", outputFilePath)

if __name__ == '__main__':
    """
    Starting of the execution
    """
    main(const.CUSTOMER_FILE_PATH,  const.OUTPUT_FILE_PATH)