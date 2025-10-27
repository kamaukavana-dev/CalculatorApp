# importing the necessary libraries:phonenumbers,folium and opencage
from idlelib.query import Query

import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone
from API import key
from opencage.geocoder import OpenCageGeocode
import folium

#Using phonenumbers library to extract and track phonenumber
#Extracting the countries code and nationalnumber
phone = phonenumbers.parse("+254710844634")
print(phone)
valid = phonenumbers.is_valid_number(phone)
print(valid)
time = timezone.time_zones_for_geographical_number(phone)
print(time)
region = geocoder.description_for_number(phone, 'en')
print(region)
service = carrier.name_for_number(phone, 'en')
print(service)

geocoder = OpenCageGeocode(key)

Query = "Nakuru, Kenya"
result = geocoder.geocode(Query)


#print(result)
lat = result[0] ['geometry']['lat']
lng = result[0] ['geometry']['lng']
print(lat)
print(lng)

my_map = folium.Map(location=[lat, lng], zoom_start=11)
folium.Marker(location=[lat, lng], popup=region).add_to(my_map)
folium.Marker(location=[lat, lng], popup=f'{region}({service})',tooltip='phone location').add_to(my_map)

folium.Marker(location=[lat, lng], popup=f'{region}-{service}',tooltip='click').add_to(my_map)

folium.Circle(
     location=[lat, lng],
     radius=5000,
     color='red',
     fill=True,
     fill_opacity=0.2
 ).add_to(my_map)

if not valid:
     print("Sorry, something went wrong.")
     exit()

if not result:
    print("Sorry, something went wrong.")
    exit()

my_map.save('mum.html')
