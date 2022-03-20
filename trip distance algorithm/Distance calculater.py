##
#Python's program to calculate Distance Between Two Points on Earth
##
from math import radians, cos, sin, asin, sqrt
 
#Read the input from user
print("Enter the latitude and longitude of two points on the Earth in degrees:")
lat1 = float(input(" Latitude 1: "))
lon1 = float(input(" Longitude 1: "))
lat2 = float(input(" Latitude 2: "))
lon2 = float(input(" Longitude 2: "))
 
# The math module contains a function named radians which converts from degrees to radians.
lon1 = radians(lon1)
lon2 = radians(lon2)
lat1 = radians(lat1)
lat2 = radians(lat2)
 
# Haversine formula 
dlon = lon2 - lon1 
dlat = lat2 - lat1 
a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
c = 2 * asin(sqrt(a)) 
r = 6371 # Radius of earth in kilometers. Use 3956 for miles
 
#Display the result
print("Distance is: ",c*r,"Kilometers")
