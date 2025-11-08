# ✅ **Week 15 – Day 7: OpenCV Revision**

Yeh revision **pure week ki sari cheezein** ek hi jagah par summarize karega + ek small practice task bhi dunga.

---

# ✅ ✅ **1. Basic Image Loading & Display**

**Key points:**

* `cv2.imread()` → image load
* `cv2.imshow()` → show
* `cv2.imwrite()` → save
* BGR hoti hai by default (RGB nahi)

```python
img = cv2.imread("image.jpg")
cv2.imshow("Image", img)
cv2.waitKey(0)
```

✅ *Lesson:* Image load na ho to path 100% galat hota hai.

---

# ✅ ✅ **2. Drawing Shapes (Circle, Line, Rectangle)**

**Important points:**

* OpenCV BGR use karta hai → color ulta lagta hai (0,255,0) = green
* Shapes directly frame pe draw hotay hain

```python
cv2.circle(img, (150,150), 80, (0,255,0), 3)
cv2.rectangle(img, (100,70), (350,300), (255,0,0), 2)
cv2.line(img, (0,0), (300,300), (0,0,255), 2)
```

✅ *Lesson:* Agar image color change ho raha ho → BGR/RGB mismatch.

---

# ✅ ✅ **3. Basic Operations**

### ✅ Rotate

```python
rot = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
```

### ✅ Flip

```python
flip = cv2.flip(img, 1)  # 1 = horizontal
```

### ✅ Channels split

```python
b,g,r = cv2.split(img)
```

✅ *Lesson:* BGR order kabhi nahi bhoolna.

---

# ✅ ✅ **4. Blurring & Threshold**

**Gaussian Blur ka rule:**
Kernel size **odd** hota hai (3,5,7,...)

```python
blur = cv2.GaussianBlur(img, (7,7), 0)
```

**Threshold:**

```python
_, thresh = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY)
```

✅ *Lesson:* Kernel size even ho to error aata hai.

---

# ✅ ✅ **5. Edge Detection**

### ✅ Canny

```python
edges = cv2.Canny(img, 100, 200)
```

### ✅ Sobel

```python
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1)
```

✅ *Lesson:* Canny is best for clean edges.

---

# ✅ ✅ **6. Face Detection (Haarcascade)**

```python
face_data = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
faces = face_data.detectMultiScale(gray, 1.1, 4)

for (x,y,w,h) in faces:
    cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
```

✅ *Lesson:* Haarcascade grayscale require karta hai.

---

# ✅ ✅ **7. Webcam Processing**

Live processing ka formula:

```
loop → read frame → flip → apply filter → show
```

```python
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow("Live", gray)
    if cv2.waitKey(1) == ord('q'):
        break
```

✅ *Lesson:* `cv2.waitKey(1)` zaroori hai — warna video freeze.

---

# ✅ ✅ **8. Mini Project Summary (Streamlit)**

* Webcam read
* Apply Filters
* Convert to RGB
* Streamlit display

Tumne already build kar liya ✅🔥

---

# ✅ ✅ **Short Revision Summary (Quick Memory Tip)**

💡 **OpenCV ka golden formula:**

📌 *Load → Convert → Process → Draw → Show*<br>
📌 BGR ≠ RGB (color issues yahin hotay hain)<br>
📌 GaussianBlur kernel must be odd<br>
📌 Face detection requires grayscale<br>
📌 Webcam processing requires loop + waitKey<br>
📌 Streamlit uses RGB (not BGR)<br>

---
