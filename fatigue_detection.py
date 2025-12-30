import cv2
import mediapipe as mp
import time

# Face mesh (Day 3)
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(refine_landmarks=True)

cap = cv2.VideoCapture(0)

# Day 4 variables
eye_closed = False

# Day 5 additions
blink_count = 0
start_time = time.time()

BLINK_THRESHOLD = 0.004
FATIGUE_BLINK_THRESHOLD = 30

while True:
    ret, frame = cap.read()
    if not ret:
        break

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb)

    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:

            # Eye landmarks (Day 3)
            upper_eye = face_landmarks.landmark[159]
            lower_eye = face_landmarks.landmark[145]

            eye_distance = abs(upper_eye.y - lower_eye.y)

            # Blink logic (Day 4)
            if eye_distance < BLINK_THRESHOLD:
                eye_closed = True
            else:
                if eye_closed:
                    blink_count += 1   # Day 5 extension
                eye_closed = False

    elapsed_time = time.time() - start_time

    # Fatigue decision (Day 5)
    if elapsed_time >= 60:
        if blink_count > FATIGUE_BLINK_THRESHOLD:
            status = "FATIGUE DETECTED"
        else:
            status = "NORMAL"

        blink_count = 0
        start_time = time.time()
    else:
        status = "Monitoring..."

    cv2.putText(frame, status,
                (30, 50),
                cv2.FONT_HERSHEY_SIMPLEX,
                1.2,
                (0, 0, 255),
                3)

    cv2.imshow("Day 5 - Fatigue Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
