# ✅ **Day 5 – Webcam Processing (OpenCV)**

```python
import cv2

# Open webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # ----- Filters -----
    # 1️⃣ Grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 2️⃣ Canny Edge Detection
    edges = cv2.Canny(gray, 100, 200)

    # 3️⃣ Sketch effect
    inv_gray = 255 - gray
    blur = cv2.GaussianBlur(inv_gray, (21, 21), 0)
    sketch = cv2.divide(gray, 255 - blur, scale=256)

    # ----- Display -----
    cv2.imshow("Original", frame)
    cv2.imshow("Grayscale", gray)
    cv2.imshow("Edges", edges)
    cv2.imshow("Sketch", sketch)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
```

---

# ✅ **Explanation**

### 1️⃣ Grayscale

* Converts color image to black & white
* Useful for filters & reducing computation

### 2️⃣ Edge Detection (Canny)

* Detects edges in image
* Parameters: minVal=100, maxVal=200

### 3️⃣ Sketch Effect

* Inverts grayscale → applies Gaussian blur → divide
* Gives pencil sketch look

---

# ✅ **Task for you**

1. Run webcam and see all filters in real-time.
2. Experiment with `cv2.Canny()` thresholds (50-150, 200-300).
3. Change Gaussian blur kernel size (15, 21, 31) to see effect on sketch.

---
