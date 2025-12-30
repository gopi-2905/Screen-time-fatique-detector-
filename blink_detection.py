import cv2
import mediapipe as mp
import time

# Initialize Face Mesh
face_mesh = mp.face_mesh.FaceMesh(
    max_num_faces=1,
    refine_landmarks=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

cap = cv2.VideoCapture(0)

blink_count = 0
eye_closed = False
start_time = time.time()
FATIGUE_BLINK_THRESHOLD = 20  # Threshold for eye fatigue

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert BGR to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process face landmarks
    results = face_mesh.process(rgb_frame)

    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            # Get specific landmarks for left and right eyes
            left_eye = face_landmarks.landmark[159]
            right_eye = face_landmarks.landmark[145]

            # Simple blink detection logic
            if abs(left_eye.y - right_eye.y) < 0.004:
                if not eye_closed:
                    blink_count += 1
                    eye_closed = True
            else:
                eye_closed = False

    elapsed_time = time.time() - start_time

    # Check every 60 seconds
    if elapsed_time >= 60:
        if blink_count >= FATIGUE_BLINK_THRESHOLD:
            status = "FATIGUE DETECTED! Take a break"
        else:
            status = "NORMAL"
        blink_count = 0
        start_time = time.time()
    else:
        status = "Monitoring..."

    # Display status on frame
    cv2.putText(frame, status,
                (30, 50), cv2.FONT_HERSHEY_SIMPLEX,
                1.2, (0, 0, 255), 3)

    cv2.imshow("Blink & Fatigue Detection", frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
