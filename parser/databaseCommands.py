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

	connection = sql.connect("parser/trackData.db")
	cursor = connection.cursor()

	cursor.execute('''
	INSERT INTO Runs (date, distance, duration, avg_pace, elevation_gain)
	VALUES (?, ?, ?, ?, ?)
	''', (track.date, track.distance, track.duration, track.avg_pace, track.elevation_gain))

	connection.commit()
	connection.close()


def queryData():

	connection = sql.connect("parser/trackData.db")
	cursor = connection.cursor()

	cursor.execute('SELECT * FROM Runs')
	rows = cursor.fetchall()

	connection.close()

	return rows