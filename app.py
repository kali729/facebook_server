from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from datetime import datetime
import urllib.parse

from flask_pymongo import PyMongo

from pymongo import MongoClient
from datetime import datetime, timezone


app = Flask(__name__)
CORS(app)


username = urllib.parse.quote_plus('sftghsffth')

password = urllib.parse.quote_plus('giHkXMkhFVwBdfLb')

# Initialize MongoDB collections MongoDB Atlas connection string


app.config["MONGO_URI"] = f"mongodb+srv://{username}:{password}@cluster0.m8r2cjv.mongodb.net/dbname?retryWrites=true&w=majority"

mongo = PyMongo(app)

db = mongo.db

collection = db['facebook']

@app.route('/submit', methods=['POST'])
def submit_data():
    data = request.json  # Get the JSON data sent from the client
    print("Received data:", data)
    
    # Add a timestamp
    data['timestamp'] = datetime.now(timezone.utc)
    
    # Save to MongoDB
    try:
        result = collection.insert_one(data)
        return jsonify({"status": "success", "message": "Data saved successfully!", "id": str(result.inserted_id)})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
