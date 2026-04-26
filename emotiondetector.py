import cv2
from deepface import DeepFace

cap = cv2.VideoCapture(0)

frame_count = 0
emotion = "Detecting..."

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Run AI every 10 frames (faster)
    if frame_count % 10 == 0:
        try:
            result = DeepFace.analyze(
                frame,
                actions=['emotion'],
                enforce_detection=False
            )
            emotion = result[0]['dominant_emotion']
        except Exception as e:
            print("Error:", e)

    frame_count += 1

    # Display emotion
    cv2.putText(frame, emotion, (50, 50),
                cv2.FONT_HERSHEY_SIMPLEX,
                1, (0, 255, 0), 2)

    cv2.imshow("Emotion Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
