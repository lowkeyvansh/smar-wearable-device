from pymongo import MongoClient
from wearable_data_simulator import generate_data
import time

client = MongoClient('mongodb://localhost:27017/')
db = client['wearable_device']
data_collection = db['user_data']

def store_data(data):
    data_collection.insert_one(data)

if __name__ == "__main__":
    while True:
        data = generate_data()
        store_data(data)
        print("Data stored:", data)
        time.sleep(1)  # Simulate data collection every second
