# EV Rear-View & Collision Avoidance System

A custom-built, hardware-integrated rear monitoring system designed specifically for a competition-level Electric Vehicle (EV). This system interfaces directly with the Vehicle Control Unit (VCU) to automatically manage camera resources, streaming a low-latency feed with Augmented Reality (AR) parking guidelines and active collision warnings.

## Features
* **Direct VCU Integration:** Bypasses traditional 12V automotive reverse signals by directly reading clean 3.3V digital logic from the custom EV's central controller via GPIO.
* **Aggressive Resource Management:** Designed for edge devices (Raspberry Pi 5). The camera pipeline and OpenCV resources are completely halted and flushed from RAM when the vehicle shifts back to drive, ensuring maximum processing power is reserved for critical forward-facing ADAS tasks.
* **Custom EV HUD:** Features an integrated On-Screen Display (OSD) tailored for race environments, showing real-time VCU connection status and ultrasonic distance telemetry.
* **Sensor Fusion:** Synchronizes physical ultrasonic sensor distance data with the visual camera feed in real-time.

## Tech Stack & Hardware
* **Language:** Python 3
* **Vision & UI Overlay:** OpenCV (`cv2`)
* **Hardware Interfacing:** `gpiozero`
* **Target Environment:** Custom Electric Vehicle (TEKNOFEST EV specifications)
* **Compute Node:** Raspberry Pi 5

## Installation & Usage

1. Clone the repository:
   ```bash
   git clone [https://github.com/recepyalcinkaya/rear-view-system.git](https://github.com/recepyalcinkaya/rear-view-system.git)
   cd rear-view-system

2. Install dependencies: pip install -r requirements.txt

3. Run the system: python main.py

Note: For local testing without a VCU connected, focus the OpenCV window and press and hold the R key to simulate the VCU sending a reverse engagement signal
