import cv2
import mediapipe as mp

# Initialize MediaPipe Face Mesh
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(refine_landmarks=True)

# Open webcam
cap = cv2.VideoCapture(0)

eye_closed = False

# Blink threshold (distance between eyelids)
BLINK_THRESHOLD = 0.004

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert frame to RGB
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb)

    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:

            # Left eye landmarks
            upper_eye = face_landmarks.landmark[159]
            lower_eye = face_landmarks.landmark[145]

            # Calculate distance
            eye_distance = abs(upper_eye.y - lower_eye.y)

            # Blink detection logic
            if eye_distance < BLINK_THRESHOLD:
                eye_closed = True
            else:
                if eye_closed:
                    cv2.putText(frame, "BLINK DETECTED",
                                (30, 50),
                                cv2.FONT_HERSHEY_SIMPLEX,
                                1.2,
                                (0, 0, 255),
                                3)
                eye_closed = False

    cv2.imshow("Day 4 - Eye Blink Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
