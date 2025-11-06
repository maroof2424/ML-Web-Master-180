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
    
    # Ab image safe hai, operations start kar sakte hain
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    small = cv2.resize(img, (300, 300))
    crop = img[80:250, 50:250]
    img2 = img.copy()
    cv2.rectangle(img2, (50, 50), (200, 200), (0, 0, 255), 2)
    cv2.circle(img2, (100, 100), 40, (0, 255, 0), 2)
    cv2.putText(img2, "This is Text on image", (50, 300), 
                cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 0), 2)

    cv2.imshow("Original Image", img)
    cv2.imshow("Grayscale Image", gray)
    cv2.imshow("Small Image", small)
    cv2.imshow("Cropped Image", crop)
    cv2.imshow("Shapes and Text", img2)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:
    print("Image not found. Please check the path!")
