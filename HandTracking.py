import cv2
import mediapipe as mp
import time


def open_camera(indexes=(0, 1, 2)):
    for index in indexes:
        cap = cv2.VideoCapture(index)
        if cap.isOpened():
            print(f"Opened camera index {index}")
            return cap
        cap.release()
    return None


cap = open_camera()
if cap is None:
    raise SystemExit(
        "No camera found. Check your camera connection or try a different device index."
    )

while True:
    success, img = cap.read()
    if not success or img is None:
        print("Failed to read frame from camera. Exiting.")
        break

    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
