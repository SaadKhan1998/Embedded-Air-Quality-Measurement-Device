# sensor_reader.py - Handles sensor data fetching and processing

import requests
import json
import dht11
import RPi.GPIO as RPI
from collections import deque

# ThingSpeak API URL
url_feed = 'https://thingspeak.com/channels/343018/feeds.json?results=100'

temp_sensor = 4  # DHT11 Sensor GPIO Pin
TEMPERATURE_BUFFER = deque(maxlen=100)
HUMIDITY_BUFFER = deque(maxlen=100)

def fetch_data():
    """Fetch data from ThingSpeak API and parse JSON response."""
    try:
        response = requests.get(url_feed)
        response.raise_for_status()
        data = response.json()
        feed_data = data['feeds']
        return feed_data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return []

def read_dht():
    """Read temperature and humidity from DHT11 sensor."""
    instance = dht11.DHT11(pin=temp_sensor)
    result = instance.read()
    while not result.is_valid():
        result = instance.read()
    print(f"Temperature: {result.temperature} C")
    print(f"Humidity: {result.humidity} %")
    TEMPERATURE_BUFFER.append(result.temperature)
    HUMIDITY_BUFFER.append(result.humidity)
    return result.temperature, result.humidity


