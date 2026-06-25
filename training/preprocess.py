import os
import cv2
import numpy as np
from sklearn.model_selection import train_test_split

def load_dataset(data_path):
    """Load CEDAR dataset from directory structure"""
    genuine_path = os.path.join(data_path, 'full_org')
    forged_path = os.path.join(data_path, 'full_forg')
    
    images = []
    labels = []
    
    # Load genuine signatures (label = 1)
    for filename in os.listdir(genuine_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.tif')):
            img_path = os.path.join(genuine_path, filename)
            img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
            if img is not None:
                # Preprocess
                _, img = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY)
                img = cv2.resize(img, (150, 150))
                images.append(img)
                labels.append(1)  # Genuine
    
    # Load forged signatures (label = 0)
    for filename in os.listdir(forged_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.tif')):
            img_path = os.path.join(forged_path, filename)
            img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
            if img is not None:
                # Preprocess
                _, img = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY)
                img = cv2.resize(img, (150, 150))
                images.append(img)
                labels.append(0)  # Forged
    
    return  np.array(images), np.array(labels)