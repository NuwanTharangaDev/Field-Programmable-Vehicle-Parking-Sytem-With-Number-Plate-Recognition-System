from ultralytics import YOLO

model = YOLO("best.pt")  

model.predict("D:\\IMG_Processing\\config\\dataset\\images\\train\\37.jpg", save = True, save_txt = True)