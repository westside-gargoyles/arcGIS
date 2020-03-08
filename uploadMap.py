from arcgis.gis import GIS

username = 1234567654
password = input("Please enter your password:")

#new instance of GIS
gis = GIS("https://www.arcgis.com", username=username, password = password)

park_properties = {
'name':'Colorado Springs Park',
'tags':'parks, open data, world',
'type':'Shapefile'
}

#add file to gis server
data_file_location = '/home/jonathan/Desktop/Park_data.zip'
parks_shp = gis.content.add(park_properties, data=data_file_location)

# visualize the Item object `parks_shp` in rich HTML notation in your notebook.
parks_shp


#publish to a map
parks_feature_layer_item = parks_shp.publish()

#display map
parks_feature_layer_item









