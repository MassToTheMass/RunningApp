from flask import Flask, jsonify, request
from flask_cors import CORS
import os


from parser.track import Track
import parser.databaseCommands as db

db.createRunTable("trackDataTest.db")
db.clearTable("trackDataTest.db")
app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/api/reset', methods=['POST'])
def reset_database():
    db.resetTable(database_file="trackDataTest.db")
    db.createRunTable("trackDataTest.db")
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

    print(runs_data)
    print("something runnnnnnnnnnnnnnnnns")

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
    print("before run ID there is thissssssssssssssssssssssssssssss")
    runID = request.args.get("runID")
    print(runID)
    run_data = db.queryBriefRunID(runID, database_file='trackDataTest.db')
    print(run_data)

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

    print(run_dict)

    return jsonify(run_dict)

if __name__ == '__main__':
    app.run(port=5000)