from GPSPhoto import gpsphoto
import folium


def getImageData(image):

    res = gpsphoto.getGPSData(image)

    dataExist = len(res)
    if dataExist != 0:

        lat = res['Latitude']
        lon = res['Longitude']
        print(lat, lon)

        myMap = folium.Map(location=[lat, lon], zoom_start=9)
        folium.Marker(location=[lat, lon]).add_to(myMap)
        myMap.save('index.html')
    else:
        print('no data available')


getImageData('image1.jpg')
getImageData('image2.jpg')
getImageData('image3.jpg')
