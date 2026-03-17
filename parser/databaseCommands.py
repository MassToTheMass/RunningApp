import sqlite3 as sql

def createRunTable():

	connection = sql.connect("trackData.db")
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


def insertData(track_point):

	pass

def queryData():

	pass