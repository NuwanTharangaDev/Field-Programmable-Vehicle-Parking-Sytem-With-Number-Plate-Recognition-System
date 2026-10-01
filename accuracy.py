from ultralytics import YOLO

model = YOLO("best.pt")

metrics = model.val(data="config.yaml") 

print(metrics)