import folium
import pandas as pd

data  = pd.read_csv('centre_locations.csv')

latitudes = list(data.latitude)
longitudes = list(data.longitude)
location_name = list(data.location_name)


map = folium.Map(location =( 48.153552 ,-80.014725) , zoom_start = 6)


fg = folium.FeatureGroup(name = "Test Locaitons")

for lt , ln , info in zip(latitudes , longitudes , location_name):
    fg.add_child(folium.Marker(location = (lt,ln) , icon = folium.Icon(color= 'red' , icon_color = 'white' , icon = 'info-sign') , popup = info))


fgi = folium.FeatureGroup(name = "India")
fgi.add_child(folium.GeoJson(data = (open('India.Json' , 'r').read())  ))




map.add_child(fg)
map.add_child(fgi)
map.add_child(folium.LayerControl())


map.save("map.html")







print(data)
