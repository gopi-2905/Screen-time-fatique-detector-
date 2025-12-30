# Screen Time Fatigue Detection

## Abstract
- Excessive screen usage is common in daily life due to online education and digital work environments. 
- Prolonged screen exposure causes eye strain, headaches, and mental fatigue. 
- This project detects screen time fatigue using eye-related parameters such as blink rate and eye closure. 
- By analyzing real-time webcam input, the system identifies fatigue conditions and alerts the user to take breaks, promoting healthier screen habits.

## Introduction
- Continuous screen usage has increased significantly in recent years. 
- Lack of breaks during long sessions leads to physical and mental fatigue. 
- Early detection of fatigue can help prevent health issues and improve productivity. 
- This project implements a simple and effective fatigue detection system using computer vision.

## Problem Statement
- People spend long hours in front of screens without proper breaks, causing eye strain, reduced efficiency, and fatigue. 
- There is a need for an automated system to monitor screen time fatigue and alert users in real time.

## Objectives
- Detect face and eye regions using computer vision
- Calculate eye blink rate from real-time webcam input
- Identify fatigue based on predefined thresholds
- Alert the user when fatigue is detected
- Reduce screen brightness automatically when fatigue occurs

## Methodology
1. Capture real-time video using a webcam.
2. Detect face and eye regions using OpenCV and MediaPipe Face Mesh.
3. Calculate blink count and monitor eye closure patterns.
4. Determine fatigue when blink count exceeds threshold (30 blinks/minute).
5. Display alert and reduce screen brightness automatically using OS-level APIs.

## Technologies Used
- Python
- OpenCV
- MediaPipe
- NumPy
- screen-brightness-control

## Results
- Successfully detects eye blinks and calculates blink rate.
- Fatigue is detected based on blink count per minute.
- Automatic brightness reduction occurs when fatigue is identified.
- System provides live feedback with status messages ("Monitoring...", "FATIGUE DETECTED").

## Conclusion
The Screen Time Fatigue Detection system effectively identifies eye fatigue caused by prolonged screen usage.It helps users become aware of their screen habits, encouraging regular breaks and reducing eye strain.

## Future Scope
- Integrate machine learning models for improved accuracy.
- Add sound or desktop notifications for fatigue alerts.
- Extend support to mobile and web platforms.
- Monitor additional parameters such as head posture and screen distance for better fatigue prediction.
