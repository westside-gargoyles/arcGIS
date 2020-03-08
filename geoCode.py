'''
This program takes a text input, and converts it into latitude and longitude values
using arcgis python API.
'''

from arcgis.gis import GIS
from arcgis.geocoding import geocode

def main():

	#create instance of GIS
	gis = GIS()

	#starting variables
	score = ""
	x = ""
	y = ""

	#get user input for the address
	user_input = input("Please enter an address to geocode:\n")
	#geocode address
	geocode_result = geocode(address=user_input)
	#split geocode by commas
	geocode_result = str(geocode_result).split(',')
	#take only first geocode result
	geocode_result = geocode_result[:30]


	#find each value in list, store in variable
	y_next_line = False
	for line in geocode_result:
		#store 'y' as y
		if (y_next_line):
			y = line[6:len(line)-1]
			y_next_line = False
		else:
			#store 'Score' as score
			if (line[:8] == " 'Score'"):
				score = line[10:]
			#store 'x' as x
			if (line[:11] == " 'location'"):
				x = line[19:]
				#once x is found, y will be on the next line
				y_next_line = True

	#print latitide and longitude, as well as accuracy of the result
	print("\nLongitude: "+x+"\nLatitude: "+y+"\nAccuracy: "+score+"%")


if (__name__ == "__main__"):
	main()

