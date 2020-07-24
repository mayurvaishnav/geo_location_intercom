import math

class GeoLocation(object):
    """
        Model to representation of Geo Location
    """

    __MAX_VALID_LONGITUDE = 180;
    __MIN_VALID_LONGITUDE = -180;
    __MAX_VALID_LATITUDE  = 90;
    __MIN_VALID_LATITUDE  = -90;

    def __init__(self, latitude, longitude):
        self.__latitude, self.__longitude = float(latitude), float(longitude)

    def getLatitude(self): 
        return self.__latitude

    def getLongitude(self): 
        return self.__longitude

    def getRadianLatitude(self):
        if(self.validDegree(self.__latitude, self.__MIN_VALID_LATITUDE, self.__MAX_VALID_LATITUDE) is False):
            raise Exception("Invalid Latitude...")
        return math.radians(self.__latitude)

    def getRadianLongitude(self): 
        if(self.validDegree(self.__longitude, self.__MIN_VALID_LONGITUDE, self.__MAX_VALID_LONGITUDE) is False):
            raise Exception("Invalid Longitude...")
        return math.radians(self.__longitude)

    def __repr__(self):
        return f'<latitude: { self.__latitude }, longitude: {self.__longitude}>'

    @staticmethod
    def validDegree(degree, min, max):
        if degree is None:
            return False
        if degree <= max and degree >= min:
            return True
        return False
