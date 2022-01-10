import geocoder
import os
from dotenv import load_dotenv
import numpy as np
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
import opencage
from opencage.geocoder import OpenCageGeocode
import folium

load_dotenv()

PHONE_NUMBER = os.getenv('PHONE_NUMBER')

pepnumber = phonenumbers.parse(PHONE_NUMBER)
location = geocoder.description_for_number(pepnumber, 'en')

service_pro = phonenumbers.parse(PHONE_NUMBER, 'RO')
print(carrier.name_for_number(service_pro, 'en'))

# https://opencagedata.com/dashboard
key = os.getenv('GEO_KEY')

geocoder = OpenCageGeocode(key)
query = str(location)
results = geocoder.geocode(query)
# print(results)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

print(lat, lng)


myMap = folium.Map(location=[lat, lng], zoom_start=9)
folium.Marker([lat, lng], popup=location).add_to(myMap)

myMap.save('mylocation.html')
