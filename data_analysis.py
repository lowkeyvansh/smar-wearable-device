from pymongo import MongoClient
import matplotlib.pyplot as plt

client = MongoClient('mongodb://localhost:27017/')
db = client['wearable_device']
data_collection = db['user_data']

def analyze_heart_rate():
    data = data_collection.find({}, {'_id': 0, 'heart_rate': 1})
    heart_rates = [entry['heart_rate'] for entry in data]
    
    plt.plot(heart_rates)
    plt.title('Heart Rate Over Time')
    plt.xlabel('Time')
    plt.ylabel('Heart Rate')
    plt.show()

def analyze_steps():
    data = data_collection.find({}, {'_id': 0, 'steps': 1})
    steps = [entry['steps'] for entry in data]
    
    plt.plot(steps)
    plt.title('Steps Over Time')
    plt.xlabel('Time')
    plt.ylabel('Steps')
    plt.show()

if __name__ == "__main__":
    analyze_heart_rate()
    analyze_steps()
