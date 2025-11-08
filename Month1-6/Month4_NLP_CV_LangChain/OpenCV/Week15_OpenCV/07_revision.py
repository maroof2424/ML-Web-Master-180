import cv2
import numpy as np

cap = cv2.VideoCapture(0)

current_filter = "none"

def cartoon_filter(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_blur = cv2.medianBlur(gray, 7)
    edges = cv2.adaptiveThreshold(
        gray_blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, 
        cv2.THRESH_BINARY, 9, 9
    )
    color = cv2.bilateralFilter(frame, 9, 250, 250)
    cartoon = cv2.bitwise_and(color, color, mask=edges)
    return cartoon

print("Press 'g' → grayscale | 'e' → edge | 'c' → cartoon | 'q' → quit")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    if current_filter == "grayscale":
        display_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    elif current_filter == "edge":
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        display_frame = cv2.Canny(gray, 100, 200)
    elif current_filter == "cartoon":
        display_frame = cartoon_filter(frame)
    else:
        display_frame = frame

    cv2.imshow("Webcam Filters", display_frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('g'):
        current_filter = "grayscale"
    elif key == ord('e'):
        current_filter = "edge"
    elif key == ord('c'):
        current_filter = "cartoon"
    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
