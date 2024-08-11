from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017/')
db = client['wearable_device']
data_collection = db['user_data']

@app.route('/data', methods=['GET'])
def get_data():
    data = list(data_collection.find({}, {'_id': 0}).limit(100))
    return jsonify(data)

@app.route('/latest', methods=['GET'])
def get_latest_data():
    data = data_collection.find({}, {'_id': 0}).sort('timestamp', -1).limit(1)
    return jsonify(data[0]) if data else jsonify({'msg': 'No data found'})

if __name__ == '__main__':
    app.run(debug=True)
