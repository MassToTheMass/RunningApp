import numpy as np

class Track:
    def __init__(self, gpxdata):
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
        
        self.duration = self._getDuration(gpxdata)
        self.total_distance = self.cumulative_distance[-1]
        self.avg_pace = self._getAveragePace()

    def _getDuration(self, gpxdata):

        """
        Calculates the duration of the run.

        This function gathers the start and end time of a run,
        it then subtracts them and returns the result.

        :param gpxdata: Parsed gpx data.
        :return: The duration of the run as a datetime object
        """

        start_time, end_time = gpxdata.get_time_bounds()
        return (end_time - start_time)

    def _getAveragePace(self):

        """
        Calculates the speed in meters per second to store on the backend

        Converts the total duration to seconds
        then divide total distance by total seconds to get meters per second

        :return: The average speed in meters per second
        """
        
        total_seconds = self.duration.total_seconds()
        meters_per_second = self.total_distance / total_seconds

        return meters_per_second