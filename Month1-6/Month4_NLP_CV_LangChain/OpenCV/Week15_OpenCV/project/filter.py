import numpy as np    
import cv2

def to_gray(frame):
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    return gray

def to_canny(frame):
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    canny = cv2.Canny(gray,100,200)
    return canny

def to_blur(frame):
    blur = cv2.GaussianBlur(frame,(15,15),0)
    return blur

def to_sketch(frame):
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    inv_gray = cv2.bitwise_not(gray)
    blur = cv2.GaussianBlur(inv_gray,(15,15),0)
    sketch = cv2.divide(gray,255-blur,scale=256)
    return sketch