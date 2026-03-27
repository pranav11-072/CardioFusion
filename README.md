# CardioFusion Lite – Real-Time Cardiac Monitoring & Pacemaker Simulation

CardioFusion Lite is a real-time cardiac monitoring and pacemaker simulation system designed for educational and research purposes. It allows users to visualize ECG and EGM signals, simulate pacemaker behavior, and interactively adjust pacing parameters through a web-based interface.

## 🚀 Features

- Real-time **ECG & EGM waveform simulation**
- **VVI pacemaker mode** simulation
- Adjustable pacing parameters (Lower Rate Limit, sensing thresholds, etc.)
- Live **waveform visualization** using web technologies
- Optional **webcam-based heart rate detection (PPG)**
- Interactive UI with instant feedback
- Session data logging for analysis

## 🧠 How It Works

The system continuously generates cardiac signals and compares the heart rate with the configured **Lower Rate Limit (LRL)**. If the heart rate drops below this threshold, the pacemaker logic triggers an electrical pacing pulse to restore the rhythm. The updated waveform is then displayed in real time.

## 🏗️ Tech Stack

**Backend**
- Python
- Flask
- Flask-SocketIO
- Flask-SQLAlchemy / SQLite

**Frontend**
- HTML / CSS / JavaScript
- Chart.js

## ⚙️ Installation

```bash
# Clone repository
git clone https://github.com/pranav11-072/CardioFusion.git

# Navigate to project folder
cd CardioFusion

# (Recommended) Create and activate a virtual environment
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env and set a strong SECRET_KEY
```

## 🖥️ Usage

```bash
python app.py
```

Then open **http://127.0.0.1:5000** in your browser.

1. Adjust pacing parameters (LRL, sensing thresholds) in the UI.
2. Observe real-time ECG/EGM waveform behavior.
3. Optionally enable webcam-based PPG heart rate input.

## 📚 Applications

- Biomedical engineering education
- Pacemaker logic learning
- Cardiac rhythm visualization
- Research prototyping

## 🔮 Future Improvements

- Additional pacing modes (DDD, AAI)
- Machine learning-based arrhythmia detection
- Cloud data storage
- Mobile compatibility

## 📄 License

This project is released under the MIT License.
