import random
import time
import json

def simulate_heart_rate():
    return random.randint(60, 100)

def simulate_steps():
    return random.randint(0, 50)

def simulate_sleep_quality():
    return random.choice(['Good', 'Fair', 'Poor'])

def generate_data():
    data = {
        'heart_rate': simulate_heart_rate(),
        'steps': simulate_steps(),
        'sleep_quality': simulate_sleep_quality(),
        'timestamp': time.time()
    }
    return data

def main():
    while True:
        data = generate_data()
        print(json.dumps(data))
        time.sleep(1)  # Simulate data generation every second

if __name__ == "__main__":
    main()
