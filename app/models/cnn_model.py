import tensorflow as tf
import numpy as np
import cv2
import os

def load_model(model_path):
    """Load the trained model from disk"""
    if os.path.exists(model_path):
        return tf.keras.models.load_model(model_path)
    else:
        # Return a placeholder model if not trained yet
        print(f"Warning: Model not found at {model_path}")
        return None

def preprocess_image(image_path, target_size=(150, 150)):
    """Preprocess image for model input"""
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise ValueError(f"Cannot read image from {image_path}")

    # Keep inference preprocessing aligned with training pipeline.
    _, img = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY)

    # Resize
    img = cv2.resize(img, target_size)

    # Normalize and reshape
    img = img.astype('float32') / 255.0
    img = np.expand_dims(img, axis=-1)  # Add channel dimension
    img = np.expand_dims(img, axis=0)   # Add batch dimension

    return img

def predict_signature(model, image_path, reference_id=None):
    """
    Predict if signature is genuine or forged
    In production, you'd compare with reference signatures
    """
    if model is None:
        # Demo response when model not available
        return {
            'status': 'demo',
            'message': 'Model not loaded. Please train first.',
            'confidence': 0.85,
            'is_genuine': True
        }
    
    processed_img = preprocess_image(image_path)
    prediction = float(model.predict(processed_img, verbose=0)[0][0])

    # Binary classification: 1 genuine, 0 forged
    is_genuine = prediction >= 0.5
    confidence = float(prediction if is_genuine else (1.0 - prediction))

    return {
        'status': 'success',
        'is_genuine': bool(is_genuine),
        'confidence': confidence,
        'reference_id': reference_id
    }
