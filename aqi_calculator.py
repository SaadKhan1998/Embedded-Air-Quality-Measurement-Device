# aqi_calculator.py - Computes AQI based on PM values

PM25_range = [
    (0.0, 12.0, 0, 50),
    (12.1, 35.4, 51, 100),
    (35.5, 55.4, 101, 150),
    (55.5, 150.4, 151, 200),
    (150.5, 250.4, 201, 300),
    (250.5, 500.4, 301, 500)
]

PM10_range = [
    (0, 54, 0, 50),
    (55, 154, 51, 100),
    (155, 254, 101, 150),
    (255, 354, 151, 200),
    (355, 424, 201, 300),
    (425, 604, 301, 500)
]

def AQI_Calculator(concentration, breakpoints):
    """Calculate AQI based on concentration and defined breakpoints."""
    for C_low, C_high, I_low, I_high in breakpoints:
        if C_low <= concentration <= C_high:
            return I_low + ((I_high - I_low) * (concentration - C_low)) / (C_high - C_low)
    return None  # Out of range

def AQI_function(pm25_values, pm10_values):
    """Compute AQI for PM2.5 and PM10 values."""
    AQI_PM25_Array = [AQI_Calculator(v, PM25_range) for v in pm25_values]
    AQI_PM10_Array = [AQI_Calculator(v, PM10_range) for v in pm10_values]
    AQI_MAX_Array = [max(aqi25, aqi10) for aqi25, aqi10 in zip(AQI_PM25_Array, AQI_PM10_Array)]
    return AQI_PM25_Array, AQI_PM10_Array, AQI_MAX_Array

def send_to_thingspeak(AQI_PM25_Array, AQI_PM10_Array, AQI_MAX_Array):
    """Send AQI values to ThingSpeak API."""
    thingspeak_url = "https://api.thingspeak.com/update"
    thingspeak_write_key = "YOUR_WRITE_API_KEY"
    
    for i in range(len(AQI_PM25_Array)):
        payload = {
            'api_key': thingspeak_write_key,
            'field1': AQI_PM25_Array[i],
            'field2': AQI_PM10_Array[i],
            'field3': AQI_MAX_Array[i]
        }
        requests.post(thingspeak_url, params=payload)

