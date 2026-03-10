"""
This file has all of the code necessary for parsing gpx files and retrieving data.
"""

import gpxpy
import gpxpy.gpx

with open("testFiles/testActivity1.gpx") as gpx_file:
    gpx = gpxpy.parse(gpx_file)



# use this to track distance travelled and elevation changed
for track in gpx.tracks:
    for segment in track.segments:
        for point in segment.points:
            print(f'point at ({point.latitude},{point.longitude}) -> {point.elevation}')
            print(point.time.time())


def getGpxDataFromFile(gpxfile):

    """
    Parses the gpxdata using gpxpy.parse

    :param gpxfile: The gpxfile to be parsed into data
    :return: The gpx data
    """
    with open(gpxfile) as gpx_file:
        return gpxpy.parse(gpx_file)



def getDuration(gpxdata):

    """
    Calculates the duration of the run.

    This function gathers the start and end time of a run,
    it then subtracts them and returns the result.

    :param gpxdata: Parsed gpx data.
    :return: The duration of the run as a datetime object
    """

    start_time, end_time = gpx.get_time_bounds()
    return (end_time - start_time)



getDuration(gpx)
