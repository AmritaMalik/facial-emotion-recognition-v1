# Facial Emotion Recognition 🤖

A real-time facial emotion detection system that uses webcam input to identify human emotions such as Happy, Sad, Angry, and Neutral using deep learning-based face analysis.

---

## 🚀 Features

* 🎥 Real-time webcam-based emotion detection
* 😊 Detects multiple emotions (Happy, Sad, Angry, Neutral, etc.)
* ⚡ Lightweight and runs on CPU
* 🧠 Uses pre-trained deep learning model for inference

---

## 🛠️ Tech Stack

* Python
* OpenCV
* DeepFace
* NumPy

---

## ⚙️ How it works

1. Captures video from webcam
2. Detects face in each frame
3. Sends frame to DeepFace model
4. Predicts dominant emotion
5. Displays result on screen in real time

---

## ▶️ How to Run

```bash
pip install opencv-python deepface numpy
python emotiondetector.py
```

---

## 📈 Future Improvements

* Improve speed optimization for real-time performance
* Add multi-face detection support
* Add emotion history graph
* Build a GUI or web interface
