import numpy as np
import gpxpy
import gpxpy.gpx

import parser.databaseCommands as db

class Track:
    def __init__(self, file_path):

        self.file_path = file_path

        with open(file_path) as gpx_file:
            gpxdata = gpxpy.parse(gpx_file)

        lat = []
        lon = []
        elev = []
        time = []
        cumulative_distance = [0]

        points = []
        for track in gpxdata.tracks:
            for segment in track.segments:
                points.extend(segment.points)

        for i, p in enumerate(points):
            lat.append(p.latitude)
            lon.append(p.longitude)
            elev.append(p.elevation)
            time.append(p.time)

            if i > 0:
                d = points[i-1].distance_3d(p)
                cumulative_distance.append(cumulative_distance[-1] + d)

        self.lat = np.array(lat)
        self.lon = np.array(lon)
        self.elev = np.array(elev)
        self.time = np.array(time)
        self.cumulative_distance = np.array(cumulative_distance)
        
        self.date = self.time[0].date()
        self.duration = self._computeDuration(gpxdata)
        self.total_distance = self.cumulative_distance[-1]
        self.avg_pace = self._computeAverageSpeed()
        self.ascent, self.descent = self._computeAscentDescent()


    def _computeDuration(self, gpxdata):

        """
        Calculates the duration of the run.

        This function gathers the start and end time of a run,
        it then subtracts them and returns the result.

        :param gpxdata: Parsed gpx data.
        :return: The duration of the run as a datetime object
        """

        start_time, end_time = gpxdata.get_time_bounds()
        return (end_time - start_time)

    def _computeAverageSpeed(self):

        """
        Calculates the speed in meters per second to store on the backend

        Converts the total duration to seconds
        then divide total distance by total seconds to get meters per second

        :return: The average speed in meters per second
        """
        
        total_seconds = self.duration.total_seconds()
        meters_per_second = self.total_distance / total_seconds

        return meters_per_second
    
    def _computeAscentDescent(self):
        """
        Calculates the ascent and descent in meters

        A smoothing operation was performed in order to reduce meaningless elevation changes caused by +- tiny changes in elevation

        :return: Ascent and Descent of the activty
        """

        elevation_delta = np.diff(self._smoothElevation())

        ascent = np.sum(np.maximum(elevation_delta, 0))
        descent = np.sum(np.maximum(-elevation_delta, 0))

        return ascent, descent

    def _smoothElevation(self):

        """
        Smooths the elevation array

        Creates an array of [0.2, 0.2, 0.2, 0.2, 0.2]
        We then iterate over the elevation array while averaging the values.
        We take 5 values for the average which is why our array before is 0.2.
        A padding is placed in so that numpy doesn't assume 0s on the edges and add fake elevation.

        :return: A smoothed array of elevation changes
        """

        window = 5
        kernel = np.ones(window) / window

        padded = np.pad(self.elev, (window//2,), mode='edge')
        smooth = np.convolve(padded, kernel, mode="valid")

        return smooth
    
    def save_track(self):

        db.insertData(self, database_file="trackDataTest.db")