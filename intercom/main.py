import src.constants.constant as const
import src.models.geoLocation as geoLocation
from src.service.customerService import CustomerService

def main():
    """
    Main function which call all the necessary functions.
    """
    customers = CustomerService.getCustomers(const.CUSTOMER_FILE_PATH)

    if customers is None:
        print("No customer found!")
        return

    intercomLocation = geoLocation.GeoLocation(const.INTERCOM_OFFICE_LATITUDE, const.INTERCOM_OFFICE_LONGITUDE)

    print(intercomLocation.getRadianLatitude())
    print(intercomLocation.getRadianLongitude())
    customerList = CustomerService.filterCustomers(customers, intercomLocation, const.MAX_DISTANCE_KM)

    outputFilePath = CustomerService.buildOutputFile(customerList, len(customers), const.OUTPUT_FILE_PATH)

    if outputFilePath is None:
        print("Cannot write into file")
        return
    
    print("Output file created at ", outputFilePath)

if __name__ == '__main__':
    """
    Starting of the execution
    """
    main()