![Live Demo](./assets/Traffic_light_detection_gif.gif)

# 🚦 Traffic Light Detection & Audio Alert System

A real-time deep learning module designed for the ADAS suite. This system utilizes a custom-trained YOLOv8 model to detect and classify traffic lights. It features an integrated Human-Machine Interface (HMI) that provides immediate text-to-speech (TTS) audio feedback to the driver/pilot when a green light is detected.

## 🚀 Key Features
* **Custom YOLOv8 Inference:** High-speed real-time detection optimized for standard webcams and edge devices.
* **Audio Feedback (TTS):** Integrates `pyttsx3` to act as an in-cabin vocal assistant. It audibly alerts the driver ("Yeşil yandı" / "Green light") the moment the light changes, minimizing driver distraction and reaction time.
* **State Management:** Implements flag-based state tracking to ensure the audio alert triggers only exactly at the moment of state transition (preventing audio spam while the light remains green).

## 🛠️ Tech Stack
* **Deep Learning:** Ultralytics YOLOv8, PyTorch
* **Computer Vision:** OpenCV (`cv2`)
* **Audio Engineering:** `pyttsx3` (Offline Text-to-Speech Engine)
* **Language:** Python 3

## ⚙️ Installation & Usage

1. Clone the repository and navigate to the module:
   ```bash
   cd traffic_lights_detection_system

2. Install dependencies: pip install -r requirements.txt

3. Important - Model Setup: Ensure your custom-trained YOLOv8 weights file is named best.pt and placed inside the models/ directory.

4. Run the system: python src/main.py
