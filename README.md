# Geo Location Intercom Test

Project is built on Python without any framework

## How to setup
1. `git clone https://github.com/mayurvaishnav/geo_location_intercom.git`
2. `cd geo_location_intercom`


## How to run
1. `python intercom/main.py` - to run the actual project
2. `python -m unittest discover intercom/test` - To run tests

## TechStack
1. Python
2. Unittest for unit testing, integration testing and mock

## Output
<pre>
Total Customers: 32
Customer within 100 KM: 16

[
{ "user_id": 4 "name: " Ian Kehoe "latitude: " 53.2451022 "longitude: " -6.238335 } 
{ "user_id": 5 "name: " Nora Dempsey "latitude: " 53.1302756 "longitude: " -6.2397222 } 
{ "user_id": 6 "name: " Theresa Enright "latitude: " 53.1229599 "longitude: " -6.2705202 } 
{ "user_id": 8 "name: " Eoin Ahearn "latitude: " 54.0894797 "longitude: " -6.18671 } 
{ "user_id": 11 "name: " Richard Finnegan "latitude: " 53.008769 "longitude: " -6.1056711 } 
{ "user_id": 12 "name: " Christina McArdle "latitude: " 52.986375 "longitude: " -6.043701 } 
{ "user_id": 13 "name: " Olive Ahearn "latitude: " 53 "longitude: " -7 } 
{ "user_id": 15 "name: " Michael Ahearn "latitude: " 52.966 "longitude: " -6.463 } 
{ "user_id": 17 "name: " Patricia Cahill "latitude: " 54.180238 "longitude: " -5.920898 } 
{ "user_id": 23 "name: " Eoin Gallagher "latitude: " 54.080556 "longitude: " -6.361944 } 
{ "user_id": 24 "name: " Rose Enright "latitude: " 54.133333 "longitude: " -6.433333 } 
{ "user_id": 26 "name: " Stephen McArdle "latitude: " 53.038056 "longitude: " -7.653889 } 
{ "user_id": 29 "name: " Oliver Ahearn "latitude: " 53.74452 "longitude: " -7.11167 } 
{ "user_id": 30 "name: " Nick Enright "latitude: " 53.761389 "longitude: " -7.2875 } 
{ "user_id": 31 "name: " Alan Behan "latitude: " 53.1489345 "longitude: " -6.8422408 } 
{ "user_id": 39 "name: " Lisa Ahearn "latitude: " 53.0033946 "longitude: " -6.3877505 } 
]

</pre>

The output is printed as well as stored in /output/output.txt file.