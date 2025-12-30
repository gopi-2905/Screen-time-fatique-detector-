# final Report

## Abstract
Excessive screen usage has become common in daily life due to online education and digital work environments. 
Prolonged screen exposure leads to eye strain, reduced concentration, and mental fatigue. 
This project aims to detect screen time fatigue using eye-related parameters such as blink rate and eye closure.
By analyzing real-time webcam input, the system identifies fatigue conditions and alerts the user to take breaks, promoting healthier screen usage habits.

## Introduction
In recent years, continuous screen usage has increased significantly.
Lack of breaks during long screen sessions causes physical and mental fatigue.
Early detection of fatigue can help prevent health issues and improve productivity.
 This project focuses on building a simple and effective fatigue detection system using computer vision techniques.

## Problem Statement
People spend long hours in front of digital screens without proper breaks.
This leads to eye fatigue, headaches, and reduced efficiency.
There is a need for an automated system to detect screen time fatigue and alert users in real time.

## Objectives
- To detect face and eye regions using computer vision
- To calculate eye blink rate using facial landmarks
- To identify fatigue based on predefined threshold values
- To alert the user when fatigue is detected

## Methodology
The system captures real-time video using a webcam.
Face and eye regions are detected using OpenCV and MediaPipe Face Mesh.
Eye blink count is calculated by monitoring eye closure patterns.
Fatigue is detected based on blink rate thresholds.
When fatigue is identified, an alert message is displayed to the user.

## Technologies Used
- Python
- OpenCV
- MediaPipe
- NumPy
- Computer Vision techniques

## Results
The system successfully detects eye blinks and monitors blink rate.
Based on the threshold values, the system classifies the user state as normal or fatigued. An alert message is displayed when fatigue conditions are met.

## Conclusion
The Screen Time Fatigue Detection system provides a simple and effective solution to identify fatigue caused by prolonged screen usage.
It helps users become aware of their screen habits and encourages taking regular breaks to reduce eye strain and mental fatigue.

## Future Scope
- Integration of machine learning models for improved accuracy
- Addition of sound or desktop notification alerts
- Support for mobile and web-based platforms
- Analysis of additional parameters such as head posture and screen distance
