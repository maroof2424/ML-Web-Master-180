# ✅ **Day 3 – Filters & Edge Detection (Full Code)**

```python
import cv2
import numpy as np

# --- Load Image ---
img = cv2.imread("sample.jpg")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("Original", img)
```

---

# ✅ **1) Gaussian Blur**

```python
blur = cv2.GaussianBlur(img, (7,7), 0)
cv2.imshow("Gaussian Blur", blur)
```

✅ Why?
• Noise smooth karta hai
• Edges soft hotay hain
• Canny ja Sobel se pehle blur best hota hai

---

# ✅ **2) Canny Edge Detection**

```python
edges = cv2.Canny(img_gray, 100, 200)
cv2.imshow("Canny Edges", edges)
```

✅ Notes
• First threshold = weak edges
• Second threshold = strong edges
• Pehle Gaussian blur karna recommended hai

---

# ✅ **3) Sobel Filters**

### ✅ Sobel X (vertical edges)

```python
sobelx = cv2.Sobel(img_gray, cv2.CV_64F, 1, 0, ksize=3)
sobelx = cv2.convertScaleAbs(sobelx)
cv2.imshow("Sobel X", sobelx)
```

### ✅ Sobel Y (horizontal edges)

```python
sobely = cv2.Sobel(img_gray, cv2.CV_64F, 0, 1, ksize=3)
sobely = cv2.convertScaleAbs(sobely)
cv2.imshow("Sobel Y", sobely)
```

### ✅ Combined Sobel

```python
sobel_combined = cv2.bitwise_or(sobelx, sobely)
cv2.imshow("Sobel Combined", sobel_combined)
```

---

# ✅ **4) Wait & Close**

```python
cv2.waitKey(0)
cv2.destroyAllWindows()
```

---

# ✅ Tumhara Task (Day 3)

### ✅ 1. Canny threshold experiment

Try values:

```
50,150
100,200
150,250
```

Dekho edges kitne detect hotay hain.

### ✅ 2. Sobel ksize try karo

```
3, 5, 7
```

Big kernel = stronger edges
Small kernel = thin edges

### ✅ 3. Blur + Canny combine karo

```
blur → edge detection
```

Image bohat smooth ho jati hai → kam noise.

---