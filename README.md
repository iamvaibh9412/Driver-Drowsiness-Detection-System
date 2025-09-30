# Driver-Drowsiness-Detection-System

Overview

The Driver Drowsiness Detection System is a real-time application designed to monitor a driver’s alertness while driving. Using computer vision and OpenCV, the system detects a driver’s face and eyes, and determines whether the driver is awake or sleeping. If the eyes remain closed for more than 10 seconds, the system classifies the driver as “Sleeping” and triggers visual alerts to prevent accidents.

This project is implemented with Python and is deployable as a Streamlit web app, allowing for easy integration with dashboards or vehicle infotainment systems.

🔹 Features

Real-time face and eye detection using OpenCV Haar Cascades.

Continuous awake/sleeping monitoring with visual alerts.

Console logs show repeated status updates: Sleeping Sleeping Sleeping / Awake Awake Awake.

On-screen warning: “⚠️ Driver is Sleeping! GET UP GET UP!” when drowsiness is detected.

Lightweight and dependency-free (no dlib or deep learning models required).

Deployable as a Streamlit web app for easy interaction and monitoring.

🔹 Use Case

Driver drowsiness is a major cause of road accidents worldwide. Fatigue, long drives, and insufficient rest increase the risk of sleep-related accidents. This system is designed for:

Personal vehicles: Keep drivers alert during long journeys.

Fleet management: Monitor commercial drivers to reduce accidents and improve safety.

Research and development: Integration with smart cars, IoT devices, and advanced driver-assistance systems (ADAS).

By alerting drivers before they fall asleep, this system can significantly reduce the risk of collisions and save lives.

🔹 How It Works

Face Detection:
The system uses OpenCV Haar Cascades to detect the driver’s face in real-time.

Eye Detection:
Eyes are detected within the face bounding box.

Sleep Detection Logic:

If eyes remain closed for more than 10 seconds, the system classifies the driver as Sleeping.

If eyes are open, the driver is classified as Awake.

Alerts:

Visual feedback is shown on the screen using bounding boxes and text messages.

Status is continuously logged in the console.

🔹 Future Enhancements

Add audio alarm for stronger driver alerts.

Integrate mobile or Raspberry Pi support for in-car deployment.

Use deep learning models to improve detection accuracy under poor lighting or occlusions.

Add sleepiness scoring and logging for fleet management analytics.

🔹 Acknowledgements

OpenCV Haar Cascade models: Pre-trained models included in OpenCV.

Streamlit: For interactive web-based deployment.
