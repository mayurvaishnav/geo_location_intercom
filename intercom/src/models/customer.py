import src.models.geoLocation as geoLocation

class Customer(object):
    """
        Model for customer with getter methods
    """

    def __init__(self, user_id, name="", latitude=0.00, longitude=0.00):
        self.__user_id, self.__name, self.__latitude, self.__longitude = user_id, name, latitude, longitude

    def getUserId(self): 
        return self.__user_id

    def getName(self): 
        return self.__name

    def getLatitude(self): 
        return self.__latitude

    def getLongitude(self): 
        return self.__longitude

    def __repr__(self):
        return f'<user_id: { self.__user_id }, name: {self.__name}>'

    def getLocation(self):
        return geoLocation.GeoLocation(self.__latitude, self.__longitude)