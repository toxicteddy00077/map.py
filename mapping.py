import folium
import pandas


data=pandas.read_csv("Volcanoes.txt")
lat=list(data["LAT"])
lon=list(data["LON"])
elev=list(data["ELEV"])


fg=folium.FeatureGroup(name="My Map")

def color_producer(elevation):
    if elevation<1000:
        return 'green'
    elif 1000<=elevation<3000:
        return 'orange'
    else:
        return 'red'
map=folium.Map(location=[38.58,-99.09], zoom_start=6, tiles="Stamen Terrain")

for lt, ln, el in zip(lat,lon,elev):
    fg.add_child(folium.CircleMarker(location=[lt,ln],radius=10,popup=str(el)+"m",fill_color=co

fg.add_child(folium.GeoJson(data=open('world.json','r',encoding='utf-8-sig'),style_function=lam
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fg)
map.save("Map2.html")
