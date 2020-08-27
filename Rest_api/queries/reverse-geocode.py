import geopy
from geopy import Nominatim

cord = (26.8393, 80.9231)

geolocator = Nominatim(user_agent='test/1')
location = geolocator.reverse('28.6995123, 77.1301047')
print(type(location.address))
print(location.address)

add = location.address

print(add.split(',')[0])
print(Nominatim(user_agent='test/1').reverse('28.6995123, 77.1301047').address.split(',')[0])