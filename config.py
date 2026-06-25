import os

class Config:
    SECRET_KEY = 'your-secret-key-change-in-production'
    UPLOAD_FOLDER = 'app/static/uploads'
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max upload
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'tif', 'tiff'}
    MODEL_PATH = 'training/saved_model/signature_model.h5'