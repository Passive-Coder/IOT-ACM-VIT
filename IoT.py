import requests
import random
import time

API_KEY = "70JVZRLZB80M93B7"
URL = "https://api.thingspeak.com/update"

while True:
    temperature = round(random.uniform(20, 35), 2)
    humidity = round(random.uniform(40, 80), 2) 
    pressure = round(random.uniform(1, 100), 2) 
    lamp_status = 1 if random.choice([True, False]) else 0

    payload = {
        "api_key": API_KEY,
        "Temperature": temperature,
        "Humidity": humidity,
        "Pressure": pressure,
        "lamp": lamp_status
    }
    
    response = requests.get(URL, params=payload)

    if response.status_code == 200:
        lamp_state = "ON" if lamp_status == 1 else "OFF"
        print(f"Data sent: Temperature={temperature}°C, Humidity={humidity}%, Pressure={pressure} hPa, Lamp={lamp_state}")
    else:
        print(f"Failed to send data: {response.status_code}")

    time.sleep(15)  
