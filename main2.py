import re
import cv2
from ultralytics import YOLO
import easyocr
import requests

reader = easyocr.Reader(['en'])

API_ENDPOINT = "http://127.0.0.1:5000/vehicle"

model = YOLO('best.pt').to('cpu')
cap = cv2.VideoCapture(0) 

pattern = r'^[A-Z]{3} \d{4}$'  
pattern2 = r'^[A-Z]{2} \d{4}$'  

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)
    annotated_frame = results[0].plot() 

    for result in results[0].boxes.xyxy:  
        x1, y1, x2, y2 = map(int, result)  
        cropped_plate = frame[y1:y2, x1:x2]  

        gray_plate = cv2.cvtColor(cropped_plate, cv2.COLOR_BGR2GRAY)

        ocr_result = reader.readtext(gray_plate, detail=0)  
        number_plate_text = " ".join(ocr_result).strip()  

        print(f"Detected Text: {number_plate_text}")

        if re.match(pattern, number_plate_text) or re.match(pattern2, number_plate_text):
            print(f"Valid Detected Text: {number_plate_text}")

            headers={
                'User-Agent': 'Mozilla/5.0',
                'Content-type':'application/json'
            }

            data = {
                'number_plate' : number_plate_text
            }

            try:
                r = requests.post(url=API_ENDPOINT, json=data, headers=headers)
            except Exception as e:
                print(e)

            cap.release()
            cv2.destroyAllWindows()

            cv2.putText(annotated_frame, f"Valid: {number_plate_text}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 3)
            cv2.imshow('Final Output', annotated_frame)

            cv2.waitKey(0)
            cv2.destroyAllWindows()
            exit() 

        cv2.rectangle(annotated_frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(annotated_frame, number_plate_text, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

    cv2.imshow('YOLOv8 Real-Time Detection', annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

