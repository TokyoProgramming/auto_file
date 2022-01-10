from GPSPhoto import gpsphoto
import folium


res = gpsphoto.getGPSData('image1.jpg')

lat = res['Latitude']
lon = res['Longitude']


myMap = folium.Map(location=[lat, lon], zoom_start=9)
folium.Marker(location=[lat, lon]).add_to(myMap)
myMap.save('index.html')
