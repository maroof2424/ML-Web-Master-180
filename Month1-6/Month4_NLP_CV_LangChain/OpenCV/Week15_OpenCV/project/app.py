import streamlit as st
import cv2
from filter import to_gray, to_canny, to_blur, to_sketch

st.title("🎥 Live Webcam Filter App")
st.write("Maroof ka OpenCV + Streamlit realtime filter project!")

filter_name = st.sidebar.selectbox(
    "Choose a Filter:",
    ("None", "Gray", "Canny Edge", "Blur", "Sketch")
)

start = st.sidebar.button("Start Webcam")

frame_slot = st.empty()

if start:
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        st.error("❌ Camera not found.")
    else:
        while True:
            ret, frame = cap.read()
            if not ret:
                st.write("Could not read frame.")
                break

            if filter_name == "Gray":
                frame = to_gray(frame)
                frame_slot.image(frame, channels="GRAY")

            elif filter_name == "Canny Edge":
                frame = to_canny(frame)
                frame_slot.image(frame, channels="GRAY")

            elif filter_name == "Blur":
                frame = to_blur(frame)
                frame_slot.image(frame, channels="BGR")

            elif filter_name == "Sketch":
                frame = to_sketch(frame)
                frame_slot.image(frame, channels="GRAY")

            else:
                frame_slot.image(frame, channels="BGR")

    cap.release()
