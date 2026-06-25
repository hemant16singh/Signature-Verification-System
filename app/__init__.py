from flask import Flask
from config import Config
import os

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Ensure upload folder exists
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    
    from app import routes
    routes.init_app(app)
    
    return app