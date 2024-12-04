import os

class Config:
    # Flask App Settings
    DEBUG = True  # Set to False in production
    SECRET_KEY = os.getenv("SECRET_KEY", "your_secret_key_here")  # Replace with an environment variable in production
    UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER", "uploads")
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16 MB max file size

    # Spoofer Settings
    MAX_ITERATIONS = 1000000  # Limit the number of pixel adjustments to prevent infinite loops
    HASH_ALGORITHM = "sha512"  # Default hash algorithm
    LOG_FILE = "spoofer.log"  # Log file path
