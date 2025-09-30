import cv2
import time
import streamlit as st

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")

def run_detection():
    cap = cv2.VideoCapture(0)

    eye_closed_time = None
    SLEEP_TIME = 10
    status = "Awake"

    stframe = st.empty()

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        eyes_detected = False
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = frame[y:y+h, x:x+w]

            eyes = eye_cascade.detectMultiScale(roi_gray)
            if len(eyes) > 0:
                eyes_detected = True
                break

        if not eyes_detected:
            if eye_closed_time is None:
                eye_closed_time = time.time()
            else:
                if time.time() - eye_closed_time >= SLEEP_TIME:
                    status = "Sleeping"
        else:
            eye_closed_time = None
            status = "Awake"

        color = (0, 0, 255) if status == "Sleeping" else (0, 255, 0)
        cv2.putText(frame, f"Status: {status}", (30, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)

        if status == "Sleeping":
            cv2.putText(frame, "Driver is Sleeping! Get up! Get up!",
                        (50, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)

        # Show in Streamlit
        stframe.image(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB), channels="RGB")

    cap.release()

# Streamlit UI
st.title("🚗 Driver Drowsiness Detection System")
st.write("This system alerts if the driver closes eyes for more than 10 seconds.")
if st.button("Start Detection"):
    run_detection()
