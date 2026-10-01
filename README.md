# Number Plate Detection using YOLOv8

A computer vision project for detecting **vehicle number plates** from images using the **YOLOv8 object detection framework** provided by Ultralytics.

The project includes a custom annotated dataset, YOLOv8 model training, validation/accuracy evaluation, image prediction, and a trained model (`best.pt`).

## 📌 Project Overview

The main objective of this project is to automatically identify the location of a vehicle number plate in an image.

The model is trained as a single-class object detector:

- **Class:** `number-plate`
- **Framework:** Ultralytics YOLOv8
- **Model configuration:** `yolov8n.yaml`
- **Training epochs:** 100
- **Trained weights:** `best.pt`

The project can be used as a foundation for applications such as:

- Automatic number-plate localization
- Vehicle monitoring systems
- Parking management systems
- Traffic monitoring
- License-plate recognition pipelines
- Intelligent transportation systems

> **Note:** This project performs **number-plate detection**. It does not currently implement OCR/text recognition of the characters on the detected plate.

---

## 🛠️ Technologies Used

- **Python**
- **YOLOv8**
- **Ultralytics**
- **PyTorch**
- **OpenCV**
- **NumPy**
- **Pandas**
- **Matplotlib**
- **PyYAML**

The dependency versions used in the project are listed in `requirements.txt`.

---

## 📂 Project Structure

```text
.
├── accuracy.py
├── best.pt
├── config.yaml
├── main.py
├── predict.py
├── requirements.txt
│
├── dataset/
│   ├── images/
│   │   └── train/
│   │       └── *.jpg
│   │
│   └── labels/
│       └── train/
│           └── *.xml
│
└── runs/
    └── detect/
        ├── predict/
        │   ├── 11.jpg
        │   └── labels/
        │       └── 11.txt
        │
        └── val/
            ├── confusion_matrix.png
            ├── confusion_matrix_normalized.png
            ├── val_batch0_labels.jpg
            ├── val_batch0_pred.jpg
            ├── val_batch1_labels.jpg
            ├── val_batch1_pred.jpg
            ├── val_batch2_labels.jpg
            └── val_batch2_pred.jpg
```

The uploaded project contains **251 training images** and **251 XML annotation files**.

---

## ⚙️ How It Works

The workflow is divided into three main stages:

### 1. Model Training

`main.py` loads the YOLOv8 nano model configuration and trains it using the dataset configuration.

```python
from ultralytics import YOLO

model = YOLO("yolov8n.yaml")

results = model.train(data="config.yaml", epochs=100)
```

The model learns to locate number plates in the training images.

### 2. Model Validation

`accuracy.py` loads the trained `best.pt` model and evaluates it using the dataset configuration.

```python
from ultralytics import YOLO

model = YOLO("best.pt")

metrics = model.val(data="config.yaml")

print(metrics)
```

The repository also contains validation outputs such as:

- Confusion matrix
- Normalized confusion matrix
- Validation batch labels
- Validation batch predictions

### 3. Prediction

`predict.py` loads the trained model and performs detection on an image.

```python
from ultralytics import YOLO

model = YOLO("best.pt")

model.predict(
    "path/to/image.jpg",
    save=True,
    save_txt=True
)
```

The prediction process generates an image containing the detected bounding boxes and can also save detection coordinates as a text file.

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
cd YOUR-REPOSITORY
```

Replace the repository URL with your actual GitHub repository URL.

### 2. Create a virtual environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

Linux/macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🗃️ Dataset Configuration

The dataset configuration is stored in `config.yaml`.

```yaml
path: C:\Users\HP\Desktop\number plate\dataset
train: images/train
val: images/train

names:
  0: number-plate
```

### Important

The original `config.yaml` contains a **local Windows path**. When moving this project to another computer or GitHub repository, update the `path` value to match your local dataset location.

For example:

```yaml
path: ./dataset
train: images/train
val: images/train

names:
  0: number-plate
```

This relative-path version is recommended when the `dataset` folder is included in the repository.

> The current project configuration uses the same image folder for both `train` and `val`. For a production-quality model evaluation, it is recommended to create separate training and validation sets.

---

## 🧠 Training the Model

After configuring the dataset, run:

```bash
python main.py
```

The training script uses:

```text
YOLOv8 Nano
100 epochs
```

After training, the resulting weights can be used for prediction and validation.

The repository already includes a trained model:

```text
best.pt
```

---

## 📊 Model Evaluation

To evaluate the trained model:

```bash
python accuracy.py
```

The validation results can include metrics such as:

- Precision
- Recall
- mAP50
- mAP50-95
- Confusion matrix

The generated visual evaluation files are stored under:

```text
runs/detect/val/
```

---

## 🔍 Running Detection

Update the image path in `predict.py` or use your own image path:

```python
from ultralytics import YOLO

model = YOLO("best.pt")

model.predict(
    "path/to/your/image.jpg",
    save=True,
    save_txt=True
)
```

Then run:

```bash
python predict.py
```

The detected image and label output will be generated by Ultralytics.

---

## 📦 Main Files

| File | Purpose |
|---|---|
| `main.py` | Trains the YOLOv8 model |
| `predict.py` | Performs number-plate detection |
| `accuracy.py` | Validates and evaluates the trained model |
| `config.yaml` | Defines dataset paths and class names |
| `best.pt` | Trained YOLOv8 model weights |
| `requirements.txt` | Python dependency versions |
| `dataset/` | Training images and annotations |
| `runs/` | Training/validation/prediction outputs |

---

## 🎯 Detected Object

The model currently detects one object class:

```text
0 → number-plate
```

The detection result is represented by a bounding box around the detected number plate.

---

## 🔮 Future Improvements

Possible improvements for this project include:

- Add a dedicated validation and test dataset
- Improve dataset diversity and annotation quality
- Add real-time webcam/video detection
- Integrate OCR to read the characters on detected plates
- Build a complete Automatic Number Plate Recognition (ANPR) system
- Add confidence-score filtering
- Create a web or desktop interface
- Deploy the trained model as an API
- Optimize the model for edge devices

---

## ⚠️ Limitations

- The current implementation focuses on **number-plate detection**, not character recognition.
- The provided dataset configuration uses the training image directory as the validation directory.
- The original configuration contains a machine-specific Windows dataset path and should be changed when running on another computer.
- Detection performance depends on image quality, lighting, camera angle, plate visibility, and the diversity of the training dataset.

---

## 👨‍💻 Author

**S.D Nuwan Tharanga**


---

## 📄 License

This project is intended for educational and academic use.


