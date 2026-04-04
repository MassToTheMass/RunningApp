import sqlite3 as sql

def createRunTable(database_file="runsData.db"):

	"""
	Creates a table in the database to store run data. The table includes columns for:
		- id: A unique identifier for each run (primary key, auto-incremented)
		- date: The date of the run (text, not null)
		- total_distance: The total distance of the run (real)
		- duration: The duration of the run in seconds (integer)
		- avg_pace: The average pace of the run (real)
		- ascent: The total ascent during the run (real)
	"""

	connection = sql.connect(database_file)
	cursor = connection.cursor()
	cursor.execute('''
	CREATE TABLE IF NOT EXISTS Runs
			(id INTEGER PRIMARY KEY AUTOINCREMENT, -- Run ID
			date TEXT NOT NULL,					   -- Date of the run
			total_distance REAL,				   -- Total distance in TODO: add units
			duration INTEGER,					   -- Duration in seconds
			avg_pace REAL,						   -- Average pace in TODO: add units
			ascent REAL,						   -- Total ascent in TODO: add units
			file_path TEXT NOT NULL			   	   -- File path of the original GPX file
	)
	''')

	connection.commit()
	connection.close()


def insertData(track, database_file="runsData.db"):

	"""
	Inserts a new run into the Runs table in the database. The function takes a track object as input and extracts the relevant data to be stored in the database. The data includes:
		- date: The date of the run
		- total_distance: The total distance of the run
		- duration: The duration of the run in seconds
		- avg_pace: The average pace of the run
		- ascent: The total ascent during the run
		- file_path: The file path of the original GPX file
	:param track: A track object containing the data to be inserted into the database
	:param database_file: The path to the database file (default is "runsData.db")
	"""

	connection = sql.connect(database_file)
	cursor = connection.cursor()

	cursor.execute('''
	INSERT INTO Runs (date, total_distance, duration, avg_pace, ascent, file_path)
	VALUES (?, ?, ?, ?, ?, ?)
	''', (track.date, track.total_distance, track.duration, track.avg_pace, track.ascent, track.file_path))

	connection.commit()
	connection.close()

def deleteData(run_id, database_file="runsData.db"):

	"""
	Deletes a run from the Runs table in the database based on its ID.
	:param run_id: The ID of the run to be deleted
	:param database_file: The path to the database file (default is "runsData.db")
	"""

	connection = sql.connect(database_file)
	cursor = connection.cursor()

	cursor.execute('DELETE FROM Runs WHERE id = ?', (run_id,))

	connection.commit()
	connection.close()

def clearTable(database_file="runsData.db"):
	"""
	Deletes all runs from the Runs table in the database. This function is useful for testing purposes to ensure a clean state before running tests.

	:param database_file: The path to the database file (default is "runsData.db")
	"""

	connection = sql.connect(database_file)
	cursor = connection.cursor()

	cursor.execute('DELETE FROM Runs')

	connection.commit()
	connection.close()

def queryData(database_file="runsData.db"):

	"""
	Queries all runs from the Runs table in the database and returns them as a list of tuples. Each tuple contains the data for a single run, including:
		- id: The unique identifier for the run
		- date: The date of the run
		- total_distance: The total distance of the run
		- duration: The duration of the run in seconds
		- avg_pace: The average pace of the run
		- ascent: The total ascent during the run
		- file_path: The file path of the original GPX file

	:param database_file: The path to the database file (default is "runsData.db")
	:return: A list of tuples, where each tuple contains the data for a single run
	"""

	connection = sql.connect(database_file)
	cursor = connection.cursor()

	cursor.execute('SELECT * FROM Runs')
	rows = cursor.fetchall()

	connection.close()

	return rows

def resetTable(table_name="Runs", database_file="runsData.db"):

	"""
	Resets the inputted table in the database by dropping it and recreating it. This function is useful for testing purposes to ensure a clean state before running tests.

	:param table_name: The name of the table to reset (default is "Runs")
	:param database_file: The path to the database file (default is "runsData.db")
	"""

	connection = sql.connect(database_file)
	cursor = connection.cursor()

	cursor.execute(f'DROP TABLE IF EXISTS {table_name}')
	connection.commit()

	connection.close()