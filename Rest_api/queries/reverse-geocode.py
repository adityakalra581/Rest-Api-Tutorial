import geopy
from geopy import Nominatim

cord = (26.8393, 80.9231)

geolocator = Nominatim(user_agent='test/1')
location = geolocator.reverse('28.6995123, 77.1301047')
print(type(location.address))
print(location.address)

add = location.address

## Pitampura

print(add.split(',')[0])
print(Nominatim(user_agent='test/1').reverse('28.6995123, 77.1301047').address.split(',')[0])

## Dwarka
## Complete Address: Road 224, Sector 10, Dwarka, Dwarka Tehsil, South West Delhi, Delhi, 110077, India 

print(Nominatim(user_agent='test/1').reverse("28.577813, 77.0582406").address)

## Rohini
## Complete Address: Sector 3, Sector 9, Rohini Tehsil, North West Delhi, Delhi, 110085, India

print(Nominatim(user_agent='test/1').reverse("28.7162092, 77.1170743").address)

## Chandni Chowk

print(Nominatim(user_agent='test/1').reverse("28.63177831658984, 77.24439417984154").address)

## Man Singh Road

print(Nominatim(user_agent='test/1').reverse("28.612482152364123,77.22414473180977").address)

## Noida 

print(Nominatim(user_agent='test/1').reverse("28.58601421313013,77.35868469660956").address)