from math import radians, degrees, sin, cos, asin, acos, sqrt
import src.constants.constant as const

def calculateDistanceBetweenPoints(source, target):
	"""
	Calculate the distance between tho geo location.
	For distance calculation following formula is being used:
	distance = earthRadius * deltaAngle
	where delta = acos(sin(lat1) * sin(lat2) + cos(lat1) * cos(lat2) * cos(lon2 - lon1))
	
	Parameters:
        source (GeoLocation): an object of GeoLocation
        target (GeoLocation): an object of GeoLocation

    Returns:
        (int): distance in KM

	"""
	return const.EARTH_RADIUS_KM * (
		acos(sin(source.getRadianLatitude()) * sin(target.getRadianLatitude()) + cos(source.getRadianLatitude()) * cos(target.getRadianLatitude()) * cos(source.getRadianLongitude() - target.getRadianLongitude()))
	)
