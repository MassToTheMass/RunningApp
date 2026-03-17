from parser import databaseCommands
from types import SimpleNamespace
import unittest


class TestDatabaseFunctions(unittest.TestCase):

	def test_insertDataFunction_success(self):
        
		track = SimpleNamespace()
		track.date = "2024-06-01"
		track.distance = 5.0
		track.duration = 30.0
		track.avg_pace = 6.0
		track.elevation_gain = 50.0

		databaseCommands.insertData(track)

		# Query the run back from the database
		run_data = databaseCommands.queryData()

		# Assert that the data matches what was inserted
		assert run_data[0][1] == "2024-06-01"
		assert run_data[0][2] == 5.0
		assert run_data[0][3] == 30.0
		assert run_data[0][4] == 6.0
		assert run_data[0][5] == 50.0