"""
This file has all of the code necessary for parsing gpx files and storing the data
"""

# data to get:
# date, distance, duration, elevation_gain, avg_pace

import gpxpy
import gpxpy.gpx

from track import Track


def getActivityDataFromFile(gpxfile):

    """
    Parses the gpxdata using gpxpy.parse

    :param gpxfile: The gpxfile to be parsed into data
    :return: A track object of the GPX data
    """
    with open(gpxfile) as gpx_file:
        gpx = gpxpy.parse(gpx_file)
    
    return Track(gpx)




# ------------------ Test Functionality After This ------------------- # 

activity = getActivityDataFromFile("testFiles/testActivity1.gpx")
