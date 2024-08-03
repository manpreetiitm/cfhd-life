from flask import Flask, jsonify
from pymongo import MongoClient
from prometheus_client import start_http_server, Summary

app = Flask(__name__)

# Setup MongoDB connection
client = MongoClient("mongodb://root:password@mongodb.custom-app.svc.cluster.local:27017/mydatabase")
db = client.mydatabase
collection = db.mycollection

# Metrics initialization
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')

@app.route('/items', methods=['POST'])
def create_item():
    data = request.json
    item = {'name': data['name']}
    collection.insert_one(item)
    return jsonify(item), 201

@app.route('/items', methods=['GET'])
def get_items():
    items = list(collection.find())
    return jsonify(items), 200

@app.route('/metrics')
def metrics():
    return jsonify({
        'request_time': REQUEST_TIME,
    })

@REQUEST_TIME.time()  # Decorator to measure request time
@app.route('/some-route')
def some_route():
    return "This is a sample route!"

if __name__ == '__main__':
    # Start Prometheus server before running the app
    start_http_server(8001)  # Prometheus metrics on port 8001
    app.run(host='0.0.0.0', port=5000)
