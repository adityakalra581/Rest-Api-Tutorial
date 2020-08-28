import geopy
from geopy import Nominatim

cord = (26.8393, 80.9231)

geolocator = Nominatim(user_agent='test/1')
location = geolocator.reverse('28.6995123, 77.1301047')
print(type(location.address))
print(location.address)
print(location.raw)

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
print(Nominatim(user_agent='test/1').reverse("28.612482152364123,77.22414473180977").raw)

## Noida 

print(Nominatim(user_agent='test/1').reverse("28.58601421313013,77.35868469660956").raw)


## TASK: to get county value present in address dictionary inside sample dict.

sample = {'place_id': 103767223, 'licence': 'Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright', 'osm_type': 'way',
          'osm_id': 66188357, 'lat': '28.586119125315207', 'lon': '77.3587932881799',
           'display_name': 'Sector 34, Noida, Dadri, Gautam Buddha Nagar, Uttar Pradesh, 201301, India', 
            'address': {'residential': 'Sector 34', 'city': 'Noida', 'county': 'Dadri', 'state_district': 'Gautam Buddha Nagar', 
                        'state': 'Uttar Pradesh','postcode': '201301', 'country': 'India', 'country_code': 'in'},
                         'boundingbox': ['28.5825836', '28.5870081', '77.3579537', '77.3622022']}

print(sample['address']['county'])

## Dadri

print((Nominatim(user_agent='test/1').reverse("28.58601421313013,77.35868469660956").raw)['address']['county'])