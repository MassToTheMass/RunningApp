import sqlite3 as sql

def createRunTable():

	"""
	Creates a table in the database to store run data. The table includes columns for:
		- id: A unique identifier for each run (primary key, auto-incremented)
		- date: The date of the run (text, not null)
		- distance: The total distance of the run (real)
		- duration: The duration of the run in seconds (integer)
		- avg_pace: The average pace of the run (real)
		- elevation_gain: The total elevation gain during the run (real)
	"""

	connection = sql.connect("parser/trackData.db")
	cursor = connection.cursor()
	cursor.execute('''
	CREATE TABLE IF NOT EXISTS Runs
			(id INTEGER PRIMARY KEY AUTOINCREMENT, -- Run ID
			date TEXT NOT NULL,					   -- Date of the run
			distance REAL,						   -- Total distance in TODO: add units
			duration INTEGER,					   -- Duration in seconds
			avg_pace REAL,						   -- Average pace in TODO: add units
			elevation_gain REAL					   -- Total elevation gain in TODO: add units
	)
	''')

	connection.commit()
	connection.close()


def insertData(track):

	"""
	Inserts a new run into the Runs table in the database. The function takes a track object as input and extracts the relevant data to be stored in the database. The data includes:
		- date: The date of the run
		- distance: The total distance of the run
		- duration: The duration of the run in seconds
		- avg_pace: The average pace of the run
		- elevation_gain: The total elevation gain during the run
	:param track: A track object containing the data to be inserted into the database
	"""

	connection = sql.connect("parser/trackData.db")
	cursor = connection.cursor()

	cursor.execute('''
	INSERT INTO Runs (date, distance, duration, avg_pace, elevation_gain)
	VALUES (?, ?, ?, ?, ?)
	''', (track.date, track.distance, track.duration, track.avg_pace, track.elevation_gain))

	connection.commit()
	connection.close()

def deleteData(run_id):

	"""
	Deletes a run from the Runs table in the database based on its ID.
	:param run_id: The ID of the run to be deleted
	"""

	connection = sql.connect("parser/trackData.db")
	cursor = connection.cursor()

	cursor.execute('DELETE FROM Runs WHERE id = ?', (run_id,))

	connection.commit()
	connection.close()

def clearTable():
	"""
	Deletes all runs from the Runs table in the database. This function is useful for testing purposes to ensure a clean state before running tests.
	"""

	connection = sql.connect("parser/trackData.db")
	cursor = connection.cursor()

	cursor.execute('DELETE FROM Runs')

	connection.commit()
	connection.close()


def queryData():

	"""
	Queries all runs from the Runs table in the database and returns them as a list of tuples. Each tuple contains the data for a single run, including:
		- id: The unique identifier for the run
		- date: The date of the run
		- distance: The total distance of the run
		- duration: The duration of the run in seconds
		- avg_pace: The average pace of the run
		- elevation_gain: The total elevation gain during the run
	"""

	connection = sql.connect("parser/trackData.db")
	cursor = connection.cursor()

	cursor.execute('SELECT * FROM Runs')
	rows = cursor.fetchall()

	connection.close()

	return rows