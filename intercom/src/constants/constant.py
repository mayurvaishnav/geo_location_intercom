import os

EARTH_RADIUS_KM = 6378.137;

INTERCOM_OFFICE_LATITUDE = 53.339428;

INTERCOM_OFFICE_LONGITUDE = -6.257664;

MAX_DISTANCE_KM = 100;

ROOT_DIR = os.path.dirname(os.path.abspath("README.md"))

CUSTOMER_FILE_PATH = os.path.join(ROOT_DIR, 'customers.txt')

OUTPUT_FILE_PATH = os.path.join(ROOT_DIR, 'output/output.txt')