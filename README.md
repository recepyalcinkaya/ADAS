# 🚗 Advanced Driver Assistance Systems (ADAS) Suite for EVs

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green.svg)
![Hardware](https://img.shields.io/badge/Hardware-Raspberry_Pi_5-cc2244.svg)
![Status](https://img.shields.io/badge/Status-Active_Development-brightgreen.svg)

A comprehensive, highly modular software suite for Advanced Driver Assistance Systems (ADAS), designed specifically for competition-level Electric Vehicles (e.g., TEKNOFEST EV racing). 

This repository serves as the central hub for multiple autonomous driving and vehicle safety subsystems. The architecture is built around **Edge Computing**, **Sensor Fusion**, and **Hardware-in-the-Loop (HIL)** integration, completely bypassing traditional commercial vehicle limitations by communicating directly with the Vehicle Control Unit (VCU).

## 🧩 System Modules

The suite is divided into independent, decoupled repositories/folders, allowing each system to run concurrently or independently based on the vehicle's real-time resource allocation:

| Module | Description | Key Technologies |
| :--- | :--- | :--- |
| 🛣️ **[Lane Tracking System](./lane-tracking-system)** | Real-time computer vision pipeline for lane boundary detection, perspective transformation (Bird's-Eye View), and curvature mathematical modeling. | `OpenCV`, `NumPy` |
| 🚦 **[Traffic Lights Detection](./traffic_lights_detection_system)** | Deep learning-based real-time traffic light state classification optimized for edge hardware inference. | `YOLO`, `PyTorch` |
| ⚠️ **[Blind Spot Monitoring](./blind-spot-monitoring)** | Hardware-software integrated sensor fusion (Ultrasonic/Radar) to actively alert drivers of hazards in adjacent lanes via physical mirror LEDs. | `gpiozero`, `Hardware-I/O` |
| 🔄 **[Rear-View & Collision Avoidance](./rear-view-collision-avoidance)** | VCU-triggered reverse monitoring system featuring dynamic AR parking guidelines and active distance telemetry. | `OpenCV`, `Sensor Fusion` |
| 🗺️ **[Navigation System](./navigation_system)** | Custom GPS routing and telemetry tracking module specifically designed for EV racing parameters and efficiency. | `GPS/GNSS`, `Python` |
| 🖥️ **[Vehicle Dashboard UI](./vehicle-dashboard-ui)** | The central "Infotainment" brain. A touch-enabled, low-latency interface that aggregates data from all ADAS modules for the driver. | `PyQt5`, `Linux Edge` |

## ⚙️ Architecture & Hardware Strategy

Unlike standard software-only ADAS projects, this suite is heavily integrated with physical vehicle dynamics:
* **Edge Optimized:** Designed to run on constrained environments like the **Raspberry Pi 5**, utilizing efficient memory management and frame-dropping strategies to prevent thermal throttling.
* **Direct VCU Integration:** Reads clean 3.3V digital logic directly from the custom EV's central controller, avoiding the noise of traditional 12V automotive electrical systems.
* **Modularity:** If the camera fails, the Blind Spot ultrasonic sensors continue to operate seamlessly. The Dashboard UI dynamically reflects the live status of each independent node.

## 🚀 Getting Started

To explore a specific module, navigate to its respective directory. Each module contains its own dedicated `README.md` with detailed installation instructions, wiring diagrams (if applicable), and execution commands.

```bash
# Example: Running the Dashboard UI
cd vehicle-dashboard-ui
pip install -r requirements.txt
python main.py
