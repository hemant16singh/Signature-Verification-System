# ✍️ Signature Verification System

A Deep Learning-based Signature Verification System that classifies handwritten signatures as **Genuine** or **Forged** using a Convolutional Neural Network (CNN). The application provides a simple and interactive web interface built with Flask for uploading and verifying signatures.

---

## 📌 Features

- ✅ Verify handwritten signatures
- ✅ Detect Genuine vs Forged signatures
- ✅ Deep Learning (CNN) based prediction
- ✅ User-friendly Flask web interface
- ✅ Image preprocessing before prediction
- ✅ Fast and accurate verification

---

## 🛠️ Tech Stack

### Frontend
- HTML5
- CSS3
- JavaScript

### Backend
- Python
- Flask

### Deep Learning
- TensorFlow
- Keras
- OpenCV
- NumPy

---

## 📂 Project Structure

```
Signature-Verification-System/
│
├── app/
│   ├── models/
│   ├── routes.py
│   ├── templates/
│   ├── static/
│
├── training/
│   ├── preprocess.py
│   ├── train_model.py
│
├── dataset/
├── app.py
├── config.py
├── run.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/hemant16singh/Signature-Verification-System.git
```

### Move into the project

```bash
cd Signature-Verification-System
```

### Create a virtual environment

```bash
python -m venv venv
```

### Activate virtual environment

Windows

```bash
venv\Scripts\activate
```

Linux/Mac

```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
python run.py
```

Open your browser:

```
http://127.0.0.1:5000
```

---

## 🧠 Model Information

- Model: Convolutional Neural Network (CNN)
- Framework: TensorFlow / Keras
- Input: Signature Image
- Output:
  - Genuine Signature
  - Forged Signature

---

## 📊 Workflow

```
Upload Signature
        │
        ▼
Image Preprocessing
        │
        ▼
CNN Model Prediction
        │
        ▼
Genuine / Forged Result
```

---

## 📷 Screenshots

### Home Page

> Add screenshot here

```
images/home.png
```

### Prediction Result

> Add screenshot here

```
images/result.png
```

---

## 🚀 Future Improvements

- Siamese Neural Network implementation
- Higher prediction accuracy
- Real-time signature verification
- User Authentication
- Cloud Deployment
- Mobile Application Support

---

## ⚠️ Note

The trained model (`signature_model.h5`) is **not included** in this repository because it exceeds GitHub's file size limit.

You can generate the model by running:

```bash
python training/train_model.py
```

---

## 👨‍💻 Author

**Hemant Kumar**

📧 Email: hemantkumar90916@gmail.com

🔗 LinkedIn: https://www.linkedin.com/in/hemant-singh-69481b290/

💻 GitHub: https://github.com/hemant16singh

---

## ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub.

It motivates me to build more open-source projects!







# Signature Verification Flask

Project scaffold for a Flask-based signature verification system.

## Run

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python run.py
```
