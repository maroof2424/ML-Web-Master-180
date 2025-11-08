# 🎥 Day6 - Streamlit + OpenCV Live Webcam Filter App

A simple and fun real-time webcam filter app built using **Streamlit** and **OpenCV**. This project applies different filters on your webcam feed such as **Gray**, **Canny Edge**, **Blur**, and **Sketch**.

Perfect for beginners learning **OpenCV**, **image processing**, and **Streamlit UI**.

---

## 🚀 Features

* Live webcam streaming using OpenCV
* Real-time filter selection
* Sidebar controls for easy UI
* Modular design using `filters.py`
* Beginner-friendly and extendable

---

## 🧩 Project Structure

```
webcam_app/
│── app.py
│── filters.py
│── requirements.txt
```

---

## ✅ Requirements

Install dependencies:

```bash
pip install streamlit opencv-python numpy
```

---

## ▶️ Run the App

```bash
streamlit run app.py
```

Then open the browser window Streamlit provides.

---

## 📌 filters.py Overview

This file contains all filter logic:

* Gray Filter
* Canny Edge Detection
* Gaussian Blur
* Sketch Effect

Clean and modular so you can easily add more filters.

---

## 📌 app.py Overview

* Sidebar menu for filter selection
* Start webcam button
* Displays live webcam frames updated in real-time
* Uses placeholder (`st.empty()`) to render frames smoothly

---

## 🖼️ Available Filters

### **1. Gray**

Converts frame to grayscale.

### **2. Canny Edge Detection**

Highlights edges in the frame using Canny algorithm.

### **3. Blur**

Applies Gaussian blur.

### **4. Sketch Effect**

Creates a pencil sketch-like effect using image inversion and division.

---

## 💡 Future Improvements

Here are things you can add easily:

* Cartoon Filter
* Sepia Effect
* Face Detection Overlay
* Add a “Stop Webcam” button
* Save snapshot feature
* FPS counter

---

## 👤 Author

**Maroof** — Python Developer (ML, Backend, Arduino)

This project is designed as part of your OpenCV learning roadmap.

---

## 💬 Notes

Feel free to extend this project and experiment with custom filters. OpenCV is extremely powerful and this is just the beginning!

Happy coding! 🎨📸
