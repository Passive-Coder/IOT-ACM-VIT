import requests
import random
import time

THINGSPEAK_WRITE_API_KEY = "BXIT8BFOCXBMB6A5"
THINGSPEAK_URL = "https://api.thingspeak.com/update"

def send_data():
    while True:
        temperature = round(random.uniform(20.0, 35.0), 2) 
        humidity = round(random.uniform(40.0, 80.0), 2)   

        payload = {
            'api_key': THINGSPEAK_WRITE_API_KEY,
            'field1': temperature,
            'field2': humidity
        }
        response = requests.get(THINGSPEAK_URL, params=payload)
        
        if response.status_code == 200:
            print(f"Data Sent: Temperature = {temperature}°C, Humidity = {humidity}%")
        else:
            print(f"Failed to send data. Error Code: {response.status_code}")

        time.sleep(15) 
send_data()