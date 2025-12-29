# Screen Time Fatigue Detection

Screen Time Fatigue Detection is a machine learning based project.
It helps to identify user fatigue caused by long screen usage.
The system aims to reduce eye strain and improve healthy screen habits.

## Problem Statement
People spend long hours in front of screens for study and work.
This leads to eye fatigue, headache, and loss of concentration.
There is a need for a system to detect screen time fatigue.

## Objective
- To analyze screen usage behavior
- To detect fatigue using eye-related parameters
- To alert users to take breaks

## Technologies Used
- Python
- OpenCV
- MediaPipe
- Machine Learning
- NumPy, Pandas

## Project Status
# Day 1: Problem analysis, tool selection, and GitHub repository setup completed.

# Day 2 – Dataset / Parameter Study

On Day 2, eye-related parameters such as blink rate,
eye closure duration, and head posture are studied.
These parameters are analyzed to understand screen time fatigue.
The required data and threshold values are identified.

# Day 3 – Face and Eye Detection

On Day 3, basic face and eye detection is implemented
using OpenCV Haar Cascade classifiers.
The webcam is used to detect faces and eyes in real time.
This step is important for extracting eye-related parameters.

# Day 4 – Blink Rate Detection

On Day 4, eye blink detection logic is implemented
using facial landmarks from MediaPipe.
Blink count is calculated based on eye closure detection.
This helps in measuring user fatigue during screen usage.

# Day 5 – Fatigue Detection Logic

On Day 5, fatigue detection logic is implemented
using blink rate thresholds.
The system classifies user state as normal or fatigued
based on eye blink count over time.

# Day 6 – Alert and Break Suggestion

On Day 6, an alert system is implemented.
When fatigue is detected, the system displays
a break notification to the user.
This helps in reducing prolonged screen usage.

# Day 7 – Conclusion and Future Scope

On Day 7, the project is finalized.
A summary, conclusion, and future scope are documented.
The complete system workflow is reviewed.

