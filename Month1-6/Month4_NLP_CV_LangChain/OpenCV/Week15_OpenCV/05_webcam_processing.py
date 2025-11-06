# import cv2

# cap = cv2.VideoCapture(1, cv2.CAP_FFMPEG)

# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break

#     frame = cv2.resize(frame, (640, 480))  # optional for speed
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     inv_gray = 255 - gray
#     edges = cv2.Canny(gray, 100, 200)
#     blur = cv2.GaussianBlur(inv_gray, (21, 21), 0)
#     sketch = cv2.divide(gray, 255 - blur, scale=256)

#     cv2.imshow("Original", frame)
#     cv2.imshow("Grayscale", gray)
#     cv2.imshow("InverseGrayscale", inv_gray)
#     cv2.imshow("Edges", edges)
#     cv2.imshow("Blur", blur)
#     cv2.imshow("Sketch", sketch)

#     # Press 'q' to quit
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()


import os
import cv2
from PIL import Image
import numpy as np

img_path = r"P:\Python\ML-Web-Master-180\Month1-6\Month4_NLP_CV_LangChain\OpenCV\Week15_OpenCV\content\sample.jpg"

if os.path.exists(img_path):
    img = cv2.imread(img_path)
    
    if img is None:
        print("OpenCV cannot read it. Using PIL fallback.")
        try:
            pil_img = Image.open(img_path)
            img = cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2BGR)
            print("Image loaded successfully using PIL fallback!")
        except Exception as e:
            print("Failed to load image:", e)
            exit()
    
    frame = cv2.resize(img, (640, 480))  # optional for speed
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    inv_gray = 255 - gray
    edges = cv2.Canny(gray, 100, 200)
    blur = cv2.GaussianBlur(inv_gray, (21, 21), 0)
    sketch = cv2.divide(gray, 255 - blur, scale=256)

    cv2.imshow("Original", frame)
    cv2.imshow("Grayscale", gray)
    cv2.imshow("InverseGrayscale", inv_gray)
    cv2.imshow("Edges", edges)
    cv2.imshow("Blur", blur)
    cv2.imshow("Sketch", sketch)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:
    print("Image not found. Please check the path!")
