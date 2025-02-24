# Air Quality Index (AQI) Monitoring System

## Overview
This project implements an embedded system for monitoring and visualizing the Air Quality Index (AQI) using the JoyPi development kit and Raspberry Pi. The system collects environmental data from sensors, transmits data to ThingSpeak, and displays AQI levels on a local LED matrix and seven-segment display.

## Features
- **Sensor Data Collection**: PM1.0, PM2.5, PM10, Temperature, Humidity
- **Cloud Integration**: Data retrieval and storage using ThingSpeak API
- **AQI Calculation**: Real-time AQI computation using EPA breakpoints
- **Local Visualization**:
  - Seven-segment display for numerical values
  - LED matrix for trend representation
- **User Interface**: Physical button controls to navigate between data displays
- **Data Logging**: JSON storage of historical readings
- **Plotting**: Matplotlib visualization of sensor data trends

## Installation
### Prerequisites
- Raspberry Pi with Raspbian OS
- Python 3.x installed
- Required libraries:
  'pip install requests numpy matplotlib RPi.GPIO dht11 json luma.core luma.led_matrix Adafruit-LED-Backpack'
  

## Remote Connection to JoyPi Kit
To remotely access the JoyPi kit from your computer:
1. Find the IP address of the Raspberry Pi:
   'hostname -I'
   
3. Enable SSH on Raspberry Pi:
   'sudo raspi-config'
   
   - Go to `Interfacing Options > SSH` and enable it.
4. Connect to Raspberry Pi from your computer:
   'ssh pi@<IP_ADDRESS>'

   - Default username: `pi`
   - Default password: `raspberry` (change it for security)
    
5. Transfer files using SCP:
   scp localfile.py pi@<IP_ADDRESS>:/home/pi/

## Usage
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/AQI_Monitoring_System.git
   ```
2. Navigate to the project directory:
   ```sh
   cd AQI_Monitoring_System
   ```
3. Run the main script:
   ```sh
   python src/main.py
   ```

## Configuration
- **ThingSpeak API Keys**:
  - Modify `THINGSPEAK_WRITE_KEY` in `main.py` to your private key.
- **GPIO Pin Setup**:
  - Ensure correct pin assignments in `sensor_reader.py`.

## Project Structure
```
📂 AQI_Monitoring_System
│── 📂 src
│   │── main.py          # Main execution file
│   │── utils.py         # Helper functions
│   │── aqi_calculator.py # AQI computation logic
│   │── sensor_reader.py # Sensor interfacing
│── 📂 docs
│   │── README.md        # Documentation
│   │── assignment_report.pdf
│── 📂 data
│   │── historical_aqi.json
│── .gitignore
│── requirements.txt
│── setup.sh
```

## Future Enhancements
- **AI-Based AQI Prediction** using machine learning models
- **Email/Telegram Alerts** for high AQI levels
- **Web Dashboard** for real-time visualization using Flask

## License
This project is licensed under the MIT License.

