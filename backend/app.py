from flask import Flask, jsonify, request
from flask_cors import CORS
import os


from parser.track import Track
import parser.databaseCommands as db

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/api/upload', methods=['POST'])
def upload_file():
    file = request.files['file']

    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    activity = Track(filepath)
    
    db.createRunTable("trackDataTest.db")
    activity.save_track()

    return jsonify({"message": "File uploaded successfully"})

@app.route('/api/runs', methods=['GET'])
def get_runs():

    runs = []

    db.queryData()

    return jsonify(runs)


if __name__ == '__main__':
    app.run(port=5000)