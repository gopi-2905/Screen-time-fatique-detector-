# Screen Time Fatigue Detection

Screen Time Fatigue Detection is a machine learning based project. It helps to identify user fatigue caused by long screen usage.
The system aims to reduce eye strain and improve healthy screen habits.


## Problem Statement
People spend long hours in front of screens for study, work, or gaming.This leads to eye fatigue, headaches, reduced concentration, and mental strain.There is a need for a system that automatically detects screen time fatigue and alerts users in real time.


## Objectives
- Detect face and eye regions using computer vision
- Calculate eye blink rate and monitor eye closure
- Identify fatigue based on predefined thresholds
- Alert users to take breaks or reduce screen brightness
- Promote healthy screen usage habits


## Technologies Used
- Python
- OpenCV
- MediaPipe
- NumPy
- screen-brightness-control


## Project Status

### Day 1 – Problem Analysis and GitHub Setup
- Analyzed the problem of prolonged screen usage.
- Selected tools and libraries required for implementation.
- Created GitHub repository and initialized project structure.

### Day 2 – Dataset / Parameter Study
- Studied eye-related parameters such as blink rate, eye closure duration, and head posture.
- Defined threshold values to identify normal vs. fatigued states:
  - Normal blink rate: 15–20 blinks/min
  - Eye strain threshold: >30 blinks/min
  - Action: Reduce screen brightness or alert user

### Day 3 – Face and Eye Detection
- Implemented face and eye detection using OpenCV & MediaPipe Face Mesh.
- Captured live webcam input to detect facial landmarks.
- Prepared for eye blink and fatigue monitoring.

### Day 4 – Blink Rate Detection
- Calculated eye blink count by monitoring eye closure patterns.
- Implemented logic to detect blink events using facial landmarks.
- This helps in measuring fatigue in real-time.

### Day 5 – Fatigue Detection Logic
- Monitored blink count over 1-minute intervals.
- Classified user state as Normal or Fatigued based on thresholds.
- Prepared alert triggers for fatigue detection.

### Day 6 – Alert and Brightness Control
- Implemented automatic brightness reduction when fatigue is detected.
- Displayed on-screen alert messages: "FATIGUE DETECTED" or "Monitoring…"
- Integrated `screen-brightness-control` library for OS-level brightness adjustment.

### Day 7 – Conclusion and Future Scope
- Finalized full system integration.
- Verified real-time blink detection, fatigue alert, and brightness control.
- Documented summary, conclusion, and potential improvements:
  - ML-based fatigue prediction
  - Mobile/web platform integration
  - Additional parameters like head posture and screen distance
  - Desktop or sound notifications for fatigue alerts
