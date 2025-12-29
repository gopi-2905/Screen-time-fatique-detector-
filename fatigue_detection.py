import cv2
import mediapipe as mp
import time

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(refine_landmarks=True)

cap = cv2.VideoCapture(0)

blink_count = 0
eye_closed = False
start_time = time.time()

FATIGUE_BLINK_THRESHOLD = 20   # blinks per minute

while True:
    ret, frame = cap.read()
    if not ret:
        break

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = face_mesh.process(rgb)

    if result.multi_face_landmarks:
        for face_landmarks in result.multi_face_landmarks:
            left_eye = face_landmarks.landmark[159]
            right_eye = face_landmarks.landmark[145]

            if abs(left_eye.y - right_eye.y) < 0.004:
                if not eye_closed:
                    blink_count += 1
                    eye_closed = True
            else:
                eye_closed = False

    elapsed_time = time.time() - start_time

    if elapsed_time >= 60:
        if blink_count >= FATIGUE_BLINK_THRESHOLD:
            status = "FATIGUE DETECTED"
        else:
            status = "NORMAL"

        blink_count = 0
        start_time = time.time()
    else:
        status = "Monitoring..."

    cv2.putText(frame, f"Status: {status}",
                (30, 50), cv2.FONT_HERSHEY_SIMPLEX,
                1, (0, 0, 255), 2)

    cv2.imshow("Fatigue Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
