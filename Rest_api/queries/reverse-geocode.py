import geopy
from geopy import Nominatim

# cord = (26.8393, 80.9231)

# geolocator = Nominatim(user_agent='test/1')
# location = geolocator.reverse('28.6995123, 77.1301047')
# print(type(location.address))


# print(location.address)
# ## Pitampura, Saraswati Vihar Tehsil, North West Delhi, Delhi, 110034, India

# print(location.raw)

# ## OUTPUT:

# # {'place_id': 126819895, 'licence': 'Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright',
# # 'osm_type': 'way', 'osm_id': 171545970, 'lat': '28.6998349', 'lon': '77.1302746',
# # 'display_name': 'Pitampura, Saraswati Vihar Tehsil, North West Delhi, Delhi, 110034, India',
# # 'address': {'residential': 'Pitampura', 'county': 'Saraswati Vihar Tehsil', 'state_district': 'North West Delhi', 
# # 'state': 'Delhi', 'postcode': '110034', 'country': 'India', 'country_code': 'in'},
# # 'boundingbox': ['28.6998349', '28.7015373', '77.1302746', '77.1310824']}





# add = location.address

# ## Pitampura

# print(add.split(',')[0])
# print(Nominatim(user_agent='test/1').reverse('28.6995123, 77.1301047').address.split(',')[0])

# ## Dwarka
# ## Complete Address: Road 224, Sector 10, Dwarka, Dwarka Tehsil, South West Delhi, Delhi, 110077, India 

# print(Nominatim(user_agent='test/1').reverse("28.577813, 77.0582406").address)

# ## Rohini
# ## Complete Address: Sector 3, Sector 9, Rohini Tehsil, North West Delhi, Delhi, 110085, India

# print(Nominatim(user_agent='test/1').reverse("28.7162092, 77.1170743").address)

# ## Chandni Chowk

# print(Nominatim(user_agent='test/1').reverse("28.63177831658984, 77.24439417984154").address)

# ## Man Singh Road

# print(Nominatim(user_agent='test/1').reverse("28.612482152364123,77.22414473180977").address)



# print(Nominatim(user_agent='test/1').reverse("28.612482152364123,77.22414473180977").raw)

# # {'place_id': 90444158, 'licence': 'Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright', 
# # 'osm_type': 'way', 'osm_id': 24563448, 'lat': '28.612440701413355', 'lon': '77.22472149341789', 
# # 'display_name': 'Man Singh Road, Pandara Park, New Delhi, Chanakya Puri Tehsil, Delhi, 020626, India',
# #  'address': {'road': 'Man Singh Road', 'neighbourhood': 'Pandara Park', 'city': 'New Delhi',
# #  'county': 'Chanakya Puri Tehsil', 'state': 'Delhi', 'postcode': '020626', 'country': 'India', 'country_code': 'in'}, 
# # 'boundingbox': ['28.6101804', '28.6161281', '77.2245237', '77.2249096']}


# ## Noida 

# print(Nominatim(user_agent='test/1').reverse("28.58601421313013,77.35868469660956").raw)

# # {'place_id': 104840292, 'licence': 'Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright', 
# # 'osm_type': 'way', 'osm_id': 78484405, 'lat': '28.71562240563835', 'lon': '77.11773006320338', 
# # 'display_name': 'Sector 3, Sector 9, Rohini Tehsil, North West Delhi, Delhi, 110085, India',
# #  'address': {'neighbourhood': 'Sector 3', 'suburb': 'Sector 9', 'county': 'Rohini Tehsil', 
# # 'state_district': 'North West Delhi', 'state': 'Delhi', 'postcode': '110085', 'country': 'India',
# #  'country_code': 'in'}, 'boundingbox': ['28.7067538', '28.7261294', '77.1098317', '77.1271316']}


# ## TASK: to get county value present in address dictionary inside sample dict.

# sample = {'place_id': 103767223, 'licence': 'Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright', 'osm_type': 'way',
#           'osm_id': 66188357, 'lat': '28.586119125315207', 'lon': '77.3587932881799',
#            'display_name': 'Sector 34, Noida, Dadri, Gautam Buddha Nagar, Uttar Pradesh, 201301, India', 
#             'address': {'residential': 'Sector 34', 'city': 'Noida', 'county': 'Dadri', 'state_district': 'Gautam Buddha Nagar', 
#                         'state': 'Uttar Pradesh','postcode': '201301', 'country': 'India', 'country_code': 'in'},
#                          'boundingbox': ['28.5825836', '28.5870081', '77.3579537', '77.3622022']}

# print(sample['address']['county'])

# ## Dadri

# print((Nominatim(user_agent='test/1').reverse("28.58601421313013,77.35868469660956").raw)['address']['county'])
# print(Nominatim(user_agent='test/1').reverse("28.7162092, 77.1170743").raw)



# ## Sarojini Nagar, New Delhi, Vasant Vihar Tehsil, Delhi, 110023, India
# print(Nominatim(user_agent='test/1').reverse("28.5741575,77.1953703").address)

# ## Stripping down the address.
# print(*(Nominatim(user_agent='test/1').reverse("28.5741575,77.1953703").address.split(',')[0:2]), sep=', ')

# ## Ashok Vihar
# print(Nominatim(user_agent='test/1').reverse("28.6994533, 77.1848256").raw)

# print(Nominatim(user_agent='test/1').reverse("28.6994533, 77.1848256").address.split(',')[0:3])

print(Nominatim(user_agent='test/1').reverse("28.6139391, 77.2090212").address.split(',')[0:3])


## Okhla:


print(Nominatim(user_agent='test/1').reverse("28.53968,77.2614481").raw['display_name'])

# print(Nominatim(user_agent='test/1').reverse("28.6192356,77.3705299").raw)


# print((Nominatim(user_agent='test/1').reverse("28.65381, 77.22897").raw)['address']['state'])
# print(Nominatim(user_agent='test/1').reverse("28.65381, 77.22897").address.split(', ')[0:3])
