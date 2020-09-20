#-------------------------------------------------------------
# ARGOSTrackingTool.py
#
# Description: Reads in an ARGOS tracking data file and allows
#   the user to view the location of the turtle for a specified
#   date entered via user input.
#
# Author: Masha Edmondson (mee28@duke.edu)
# Date:   Fall 2020
#--------------------------------------------------------------

#Create a variable pointing to the data file
file_name = './Data/raw/sara.txt'

#Create a file object from the file
file_object = open(file_name, 'r')

#Read contents of file into a list
line_list = file_object.readlines()

#Close the file
file_object.close()

#Pretend we read one line of data from the Sara file
lineString = line_list[100]

#Split the string into a list of data items
lineData = lineString.split()

#Extract items in list into varibles
record_id = lineData[0] # ARGOS tracking record
obs_date = lineData[2] # Observation date
obs_lc = lineData[4] # Observation location class
obs_lat = lineData[6] # Observation Latitude
obs_lon = lineData[7] #Observation Longitude

#Print the Location of Sara
print(f'Record {record_id} indicates Sara was seen at lat:{obs_lat}, lon:{obs_lon} on {obs_date}')