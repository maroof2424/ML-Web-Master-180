# 📘 **Day 1 – Intro to OpenCV**

Aaj hum 5 basic concepts cover karenge:

✅ 1. OpenCV install
✅ 2. Image read & display
✅ 3. Convert to grayscale
✅ 4. Resize / Crop
✅ 5. Draw shapes (rectangle, circle, text)

---

# ✅ **1. Install OpenCV (Colab)**

```python
!pip install opencv-python
```

---

# ✅ **2. Read & Display Image (Colab method)**

Colab normal `cv2.imshow()` support nahi karta — is liye hum use karte hain:

✅ `from google.colab.patches import cv2_imshow`

```python
import cv2
from google.colab.patches import cv2_imshow

img = cv2.imread('/content/sample.jpg')   # Upload image and use its path
cv2_imshow(img)
```

---

# ✅ **3. Convert to Grayscale**

```python
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2_imshow(gray)
```

---

# ✅ **4. Resize & Crop**

### ✔ Resize:

```python
small = cv2.resize(img, (300, 300))
cv2_imshow(small)
```

### ✔ Crop (array slicing):

```python
crop = img[50:250, 50:250]   # [y1:y2 , x1:x2]
cv2_imshow(crop)
```

---

# ✅ **5. Draw Shapes**

OpenCV BGR format use karta hai (Blue, Green, Red)

✅ Rectangle
✅ Circle
✅ Text

```python
img2 = img.copy()

# Rectangle
cv2.rectangle(img2, (50, 50), (200, 200), (0, 255, 0), 3)

# Circle
cv2.circle(img2, (150, 150), 60, (255, 0, 0), 3)

# Text
cv2.putText(img2, "OpenCV Day 1", (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)

cv2_imshow(img2)
```

---

# ✅ **Complete Day 1 Notebook Template**

```python
import cv2
from google.colab.patches import cv2_imshow

# 1. Load Image
img = cv2.imread('/content/sample.jpg')
cv2_imshow(img)

# 2. Convert to Gray
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2_imshow(gray)

# 3. Resize
resized = cv2.resize(img, (300, 300))
cv2_imshow(resized)

# 4. Crop
crop = img[50:250, 50:250]
cv2_imshow(crop)

# 5. Draw Shapes
img2 = img.copy()
cv2.rectangle(img2, (50, 50), (200, 200), (0, 255, 0), 3)
cv2.circle(img2, (150, 150), 60, (0, 0, 255), 3)
cv2.putText(img2, "Day1", (30, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)

cv2_imshow(img2)
```

---

# ✅ **Day 1 Task for Maroof**

Apne image per ye 3 tasks complete kro:

### **Task 1:**

Apne picture per ek rectangle draw kro jahan face ho.

### **Task 2:**

A picture ko crop kro sirf face portion tak.

### **Task 3:**

Text add kro → `"Maroof OpenCV Day 1"`

---
