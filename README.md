# CardioFusion Lite – Real-Time Cardiac Monitoring & Pacemaker Simulation

CardioFusion Lite is a real-time cardiac monitoring and pacemaker simulation system designed for educational and research purposes. It allows users to visualize ECG and EGM signals, simulate pacemaker behavior, and interactively adjust pacing parameters through a web-based interface.

## 🚀 Features

* Real-time **ECG & EGM waveform simulation**
* **VVI pacemaker mode** simulation
* Adjustable pacing parameters (Lower Rate Limit, sensing thresholds, etc.)
* Live **waveform visualization** using web technologies
* Optional **webcam-based heart rate detection (PPG)**
* Interactive UI with instant feedback
* Session data logging for analysis

## 🧠 How It Works

The system continuously generates cardiac signals and compares the heart rate with the configured **Lower Rate Limit (LRL)**.
If the heart rate drops below this threshold, the pacemaker logic triggers an electrical pacing pulse to restore the rhythm. The updated waveform is then displayed in real time. 

## 🏗️ Tech Stack

**Backend**

* Python
* Flask
* NumPy / SciPy
* OpenCV

**Frontend**

* HTML
* CSS
* JavaScript
* Chart.js

## 📊 System Architecture

* **Frontend:** Displays ECG/EGM waveforms and user controls
* **Backend:** Generates signals and executes pacemaker logic
* **Communication:** Real-time data streaming between client and server

## ⚙️ Installation

```bash
# Clone repository
git clone https://github.com/yourusername/CardioFusion-Lite.git

# Navigate to project folder
cd CardioFusion-Lite

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
```

## 🖥️ Usage

1. Start the server.
2. Open the application in a web browser.
3. Adjust pacing parameters (LRL, sensing thresholds).
4. Observe real-time ECG/EGM waveform behavior.

## 📚 Applications

* Biomedical engineering education
* Pacemaker logic learning
* Cardiac rhythm visualization
* Research prototyping

## 🔮 Future Improvements

* Additional pacing modes (DDD, AAI)
* Machine learning-based arrhythmia detection
* Cloud data storage
* Mobile compatibility

## 📄 License

This project is released under the MIT License.
