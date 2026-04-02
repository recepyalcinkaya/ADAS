![Kör Nokta Görseli](assets/kor_nokta.jpeg)

# Blind Spot Monitoring System (BSM)

A real-time hardware-software integrated Blind Spot Monitoring system designed for ADAS applications. This project demonstrates sensor data acquisition, dynamic distance evaluation, and multi-sensor fusion to alert drivers of hazards in adjacent lanes.

## Features
* **Hardware Abstraction:** Seamlessly runs on both real edge hardware (Raspberry Pi with GPIO sensors) and in simulation mode for local development.
* **Real-time Processing:** Continuously polls left and right proximity sensors (Ultrasonic/Radar simulated) with minimal latency.
* **Zone Evaluation Logic:** Categorizes detected objects into `CLEAR`, `WARNING` (approaching), and `DANGER` (immediate blind spot) zones based on distance thresholds.
* **Dashboard Integration Ready:** Outputs modular JSON/Dictionary states designed to be broadcasted over a CAN bus or sent directly to a Vehicle Dashboard UI.

## Tech Stack & Hardware
* **Language:** Python 3
* **Libraries:** `gpiozero`, `RPi.GPIO`
* **Target Hardware:** Raspberry Pi 5
* **Sensors:** HC-SR04 Ultrasonic Distance Sensors (Easily adaptable to short-range radar modules)

## Installation & Usage

1. Clone the repository:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/blind-spot-monitoring.git](https://github.com/YOUR_USERNAME/blind-spot-monitoring.git)
   cd blind-spot-monitoring
   
2. Install the required dependencies:
pip install -r requirements.txt

3. Run the system:
python main.py

Note: If executed on a standard PC, the system will automatically fall back to simulation mode and generate mock sensor data. 
If executed on a Raspberry Pi, it will attempt to read from the defined GPIO pins.

## System Architecture:

* **Sensor Layer:** Reads raw physical signals (time-of-flight) and converts them to metric distances.

* **Logic Layer:** Applies thresholds ($1.0m$ for Danger, $2.5m$ for Warning) to determine the threat level on both sides independently.

* **Application Layer:** Aggregates the data and triggers visual/auditory warning flags.
