import cv2
import mediapipe as mp
import time

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(
    static_image_mode=False,
    max_num_faces=1,
    refine_landmarks=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

blink_count = 0
eye_closed = False
start_time = time.time()

FATIGUE_BLINK_THRESHOLD = 20

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
            status = "TAKE A BREAK!"
        else:
            status = "NORMAL"

        blink_count = 0
        start_time = time.time()
    else:
        status = "Monitoring..."

    cv2.putText(frame, status, (30, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 3)

    cv2.imshow("Fatigue Alert System", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
