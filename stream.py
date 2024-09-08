# script to stream video and perform object detection for testing

import cv2
from ultralytics import YOLO


model = YOLO("model path")  


cap = cv2.VideoCapture("video path")
if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        break


    results = model(frame)

   
    for result in results:
        annotated_frame = result.plot()


    cv2.imshow('YOLO Object Detection', annotated_frame)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
