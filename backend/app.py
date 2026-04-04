from flask import Flask, jsonify
from parser.track import Track
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/runs', methods=['GET'])
def get_runs():

    runs = [
        {"date": "2024-06-01", "distance": 5000, "duration": "00:25:00", "avg_pace": "5:00"},
        {"date": "2024-06-02", "distance": 10000, "duration": "00:50:00", "avg_pace": "5:00"},  
    ]

    return jsonify(runs)

if __name__ == '__main__':
    app.run(port=5000)