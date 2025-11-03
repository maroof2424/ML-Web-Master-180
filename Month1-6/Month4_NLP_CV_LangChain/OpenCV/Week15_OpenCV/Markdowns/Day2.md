
# ✅ **Day 2 – Basic Operations (OpenCV)**

**⏱ Time: 45–55 min total**
**Topics:**

1. Image Rotation
2. Image Flipping
3. Color Channels (RGB/BGR)
4. Blur
5. Thresholding

---

# ✅ **1) Rotation (10 minutes)**

**Concept:**
Rotation = image ko kisi angle per ghumana using `cv2.getRotationMatrix2D`.

### ✅ Code:

```python
import cv2

img = cv2.imread("image.jpg")

h, w = img.shape[:2]
center = (w//2, h//2)

# 45 degree rotation
M = cv2.getRotationMatrix2D(center, 45, 1)
rotated = cv2.warpAffine(img, M, (w, h))

cv2.imshow("Rotated", rotated)
cv2.waitKey(0)
```

### ✅ Task:

* 45°, 90°, -30° rotation apply karo.
* Compare karo kahan cropping ho rahi hai.

---

# ✅ **2) Flipping (5 minutes)**

**Concept:**

* 0 → Vertical Flip
* 1 → Horizontal Flip
* -1 → Both

### ✅ Code:

```python
flip1 = cv2.flip(img, 1)
flip0 = cv2.flip(img, 0)
flip_1 = cv2.flip(img, -1)
```

### ✅ Task:

* Selfie image flip karo; notice karo kaise mirror effect hota.

---

# ✅ **3) Color Channels (10 minutes)**

OpenCV **BGR** use karta hai, not RGB — isi liye tumhari image **bluish hoti** hai.
Color draw functions (circle, rectangle) BGR format accept karte hain.

### ✅ Split channels:

```python
b, g, r = cv2.split(img)
cv2.imshow("Blue", b)
cv2.imshow("Green", g)
cv2.imshow("Red", r)
```

### ✅ Convert BGR → RGB:

```python
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
```

### ✅ Task:

* Show each color channel separately.
* BGR → RGB convert karo aur difference dekho.

---

# ✅ **4) Blur (10 minutes)**

### ✅ Gaussian Blur:

```python
blur = cv2.GaussianBlur(img, (15,15), 0)
```

### ✅ Median Blur:

```python
med = cv2.medianBlur(img, 5)
```

### ✅ Task:

* Gaussian vs Median compare karo (noise pe difference dekho).

---

# ✅ **5) Threshold (10 minutes)**

### ✅ Simple Threshold:

```python
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, th = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY)
```

### ✅ Adaptive Threshold:

```python
ad = cv2.adaptiveThreshold(gray,255,
                           cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                           cv2.THRESH_BINARY,11,2)
```

### ✅ Task:

* Image ko binary (black & white) bana kar edge-like effect dekho.

---

# ✅ **End of Day-2 Mini Project (5 min)**

Ek **image pipeline** banao:

✅ Read Image
✅ Rotate
✅ Flip
✅ Blur
✅ Threshold
✅ Show all results in separate windows

---