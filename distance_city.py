# Import the required library
from geopy.geocoders import Nominatim
from geopy.distance import geodesic

place_1 = str(input(''))
place_2 = str(input(''))

# Initialize Nominatim API
geolocator = Nominatim(user_agent="MyApp")

location_1 = geolocator.geocode(place_1)
location_2 = geolocator.geocode(place_2)
loc1=(location_1.latitude, location_1.longitude)
loc2=(location_2.latitude, location_2.longitude)
print(geodesic(loc1, loc2).km)