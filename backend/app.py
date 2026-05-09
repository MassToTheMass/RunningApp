from flask import Flask, jsonify, request
from flask_cors import CORS
import os


from parser.track import Track
import parser.databaseCommands as db

db.resetTable(database_file="trackDataTest.db")
db.resetTable(table_name="RunPoints", database_file="trackDataTest.db")

db.createRunTable("trackDataTest.db")
db.createRunPointsTable("trackDataTest.db")
db.clearTable("trackDataTest.db")
app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/api/reset', methods=['POST'])
def reset_database():
    db.resetTable(database_file="trackDataTest.db")
    db.createRunTable("trackDataTest.db")
    db.createRunPointsTable("trackDataTest.db")

    return jsonify({"message": "Database reset successfully"})

@app.route('/api/upload', methods=['POST'])
def upload_file():
    file = request.files['file']

    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    activity = Track(filepath)
    activity.save_track()

    return jsonify({"message": "File uploaded successfully"})

@app.route('/api/runsRecentTen', methods=['GET'])
def get_runs():
    runs_data = db.getRunsRecentTen("trackDataTest.db")

    runs = []
    for run in runs_data:
        run_dict = {
            "id": run[0],
            "date": run[1],
            "total_distance": run[2],
            "duration": run[3],
            "avg_pace": run[4],
            "ascent": run[5],
            "file_path": run[6]
        }
        runs.append(run_dict)

    return jsonify(runs)

@app.route('/api/getBriefDataFromRunID', methods=['GET'])
def getBriefDataFromRunID():
    runID = request.args.get("runID")
    run_data = db.queryBriefRunID(runID, database_file='trackDataTest.db')

    run_data = run_data[0]

    run_dict = {
        "id": run_data[0],
        "date": run_data[1],
        "total_distance": run_data[2],
        "duration": run_data[3],
        "avg_pace": run_data[4],
        "ascent": run_data[5],
        "file_path": run_data[6]
    }

    return jsonify(run_dict)

@app.route('/api/getRunDataPoints', methods=['GET'])
def getRunDataPoints():
    runID = request.args.get("runID")
    run_data_points = db.queryRunDataPointsFromRunID(runID, database_file='trackDataTest.db')

    data_point_dict = {}
    for data_point in run_data_points:
        data_point_dict[data_point[0]] = {
            "lat": data_point[1],
            "lon": data_point[2],
            "elevation": data_point[3],
            "timestamp": data_point[4].decode('utf-8') if isinstance(data_point[4], bytes) else str(data_point[4])
        }

    print("Data point dict:\n\n")
    print(data_point_dict)

    return jsonify(data_point_dict)

if __name__ == '__main__':
    app.run(port=5000)