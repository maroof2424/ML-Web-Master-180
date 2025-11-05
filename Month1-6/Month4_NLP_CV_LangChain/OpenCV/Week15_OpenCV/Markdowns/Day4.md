
# Day4 - Face Detection using Haarcascade (OpenCV)

This project demonstrates a simple and efficient way to detect human faces in an image using **Haarcascade**, a pre-trained face detection model included in OpenCV.

## 🚀 Features
- Detect faces from an image
- Draw bounding boxes around faces
- Very fast and lightweight (no GPU required)
- Uses OpenCV’s built-in Haarcascade model

---

## 📂 Project Structure
```

project/
│── haarcascade_frontalface_default.xml
│── image.jpg
│── main.py
│── README.md

````

---

## ✅ Requirements
Install required libraries:

```bash
pip install opencv-python
````

Make sure you have the file:

```
haarcascade_frontalface_default.xml
```

You can download it from OpenCV GitHub:
OpenCV → data → haarcascades

---

## ✅ How It Works (Short Explanation)

1. Load Haarcascade face detection model
2. Read the image
3. Convert it to grayscale (faster detection)
4. Detect faces using `detectMultiScale()`
5. Draw rectangles around detected faces
6. Display the final output

---

## 📘 Code

```python
import cv2

# Load Haarcascade classifier
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Read image
img = cv2.imread('image.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces
faces = face_cascade.detectMultiScale(gray, 1.3, 5)

# Draw bounding boxes
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

# Display result
cv2.imshow("Face Detection", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

---

## 🔧 Important Parameters

### `scaleFactor = 1.3`

Controls how much the image is scaled down for detection.
Smaller = more accurate but slower.

### `minNeighbors = 5`

Higher value removes false detections.
Recommended: `3–6`.

---

## ✅ Output Example

Green boxes appear around faces detected in the image.

---

## 📝 Notes

* Haarcascade works best on frontal faces.
* For real-time face detection, use your webcam with OpenCV.
* For higher accuracy in real projects, consider:

  * OpenCV DNN face detector
  * Mediapipe face detection
  * YOLO face models

---
