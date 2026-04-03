from backend.parser import databaseCommands
from types import SimpleNamespace
import unittest

# The following tests for databases are going to use a test database in order to not modify any of the actual data in the database.

class TestDatabaseFunctions(unittest.TestCase):

	def test_clearTableFunction_success(self):

		databaseCommands.clearTable("backend/parser/trackDataTest.db")

		track = SimpleNamespace()
		track.date = "2024-06-01"
		track.distance = 5.0
		track.duration = 30.0
		track.avg_pace = 6.0
		track.elevation_gain = 50.0

		databaseCommands.insertData(track, "backend/parser/trackDataTest.db")
		run_data = databaseCommands.queryData("backend/parser/trackDataTest.db")
		assert len(run_data) == 1  # Ensure there is one run in the database

		databaseCommands.clearTable("backend/parser/trackDataTest.db")
		run_data_after_clear = databaseCommands.queryData("backend/parser/trackDataTest.db")
		assert len(run_data_after_clear) == 0  # Ensure the table is empty after



	def test_insertDataFunction_success(self):

		databaseCommands.clearTable("backend/parser/trackDataTest.db")
        
		track = SimpleNamespace()
		track.date = "2024-06-01"
		track.distance = 5.0
		track.duration = 30.0
		track.avg_pace = 6.0
		track.elevation_gain = 50.0

		databaseCommands.insertData(track, "backend/parser/trackDataTest.db")

		# Query the run back from the database
		run_data = databaseCommands.queryData("backend/parser/trackDataTest.db")

		# Assert that the data matches what was inserted
		assert run_data[0][1] == "2024-06-01"
		assert run_data[0][2] == 5.0
		assert run_data[0][3] == 30.0
		assert run_data[0][4] == 6.0
		assert run_data[0][5] == 50.0

	def test_deleteDataFunction_success(self):
		
		databaseCommands.clearTable("backend/parser/trackDataTest.db")

		# First, insert a run to ensure there is something to delete
		track = SimpleNamespace()
		track.date = "2024-06-01"
		track.distance = 5.0
		track.duration = 30.0
		track.avg_pace = 6.0
		track.elevation_gain = 50.0

		databaseCommands.insertData(track, "backend/parser/trackDataTest.db")

		# Query the run back from the database to get its ID
		run_data = databaseCommands.queryData("backend/parser/trackDataTest.db")
		assert len(run_data) == 1  # Ensure there is one run in the database

		run_id = run_data[0][0]

		databaseCommands.deleteData(run_id, "backend/parser/trackDataTest.db")

		# Query the database again to ensure the run was deleted
		run_data_after_delete = databaseCommands.queryData("backend/parser/trackDataTest.db")
		assert len(run_data_after_delete) == 0