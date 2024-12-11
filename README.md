# Image Hash Spoofer

## Overview
Image Hash Spoofer is a Python-based web application that allows users to modify an image file such that its hash starts with a specific hexadecimal prefix (e.g., 0x24, 0x00) while maintaining the image's visual integrity. The application uses Flask for the backend and provides an intuitive web interface for image uploading and spoofing.

## Features
- **Web Interface**: Upload images and select a hash prefix through a user-friendly interface.
- **Hash Spoofing**: Alters the image's pixel values without affecting its visual appearance to generate a hash starting with the target prefix.
- **Supported Formats**: Accepts images in PNG, JPG, and JPEG formats.
- **Validation**: Ensures that only valid prefixes and supported file types are processed.
- **SHA-512 Hashing**: Computes the hash using the SHA-512 algorithm.

## Installation and Setup
### Prerequisites

Ensure you have the following installed:

- Python 3.8 or later
- pip (Python package manager)
- A modern web browser

### Clone the Repository

```bash
git clone https://github.com/yourusername/image-hash-spoofer.git
cd image-hash-spoofer
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Directory Structure

```
image-hash-spoofer/
├── app.py                 # Flask application entry point
├── spoofer/               # Core logic for image hash spoofing
│   ├── spoofer_core.py    # Main class handling image spoofing
│   ├── pixel_modifier.py  # Logic for pixel manipulation
│   ├── hashing.py         # SHA-512 hash computation logic
│   ├── logger.py          # Utility for logging messages
│   └── validators.py      # Input validation utilities
├── static/                # Static files (CSS, JavaScript, images)
│   └── styles.css         # Stylesheet for the web interface
├── templates/             # HTML templates
│   ├── index.html         # Main upload page
│   └── result.html        # Result page
├── uploads/               # Directory to store uploaded files
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

### Run the Application
1. Start the Flask server:

```bash
python app.py
```

2. Open your browser and navigate to:

```
http://127.0.0.1:5000
```

## How It Works
1. **User Input**:
   - Users upload an image and select a target hash prefix.
   - The application validates the prefix and file type.

2. **Image Processing**:
   - The `ImageHashSpoofer` class modifies pixel values of the image to achieve a hash that starts with the target prefix.
   - The hash is computed using the SHA-512 algorithm.

3. **Result**:
   - The modified image is generated and displayed for download.
   - The resulting hash is shown on the result page.

## Key Files and Modules
- **app.py**
  - The main Flask application:
    - Handles routes for the web interface.
    - Integrates the spoofing logic.

- **spoofer/spoofer_core.py**
  - Core logic for image hash spoofing:
    - Loads the image, modifies pixels, and verifies the resulting hash.

- **spoofer/pixel_modifier.py**
  - Contains logic to adjust pixel values randomly or sequentially.

- **spoofer/hashing.py**
  - Handles hash computation using the SHA-512 algorithm.

- **spoofer/logger.py**
  - Logs application events for debugging and monitoring.

- **spoofer/validators.py**
  - Provides input validation for file types and hash prefixes.

- **templates/**
  - HTML templates for the web interface:
    - `index.html`: Form for uploading the image and selecting the target prefix.
    - `result.html`: Displays the resulting image and hash.

- **static/styles.css**
  - CSS styles for the web interface.

- **uploads/**
  - Stores uploaded and processed images temporarily.

## Usage Instructions
1. Navigate to the homepage.
2. Upload a valid image file (PNG, JPG, or JPEG).
3. Select a target hash prefix from the dropdown menu.
4. Submit the form and wait for processing.
5. Download the modified image and view the generated hash.

## Troubleshooting
- **Hash Doesn't Match Prefix**: Ensure the target prefix is valid and the input image is not corrupted.
- **Large Images**: Processing might take longer for high-resolution images.
- **Browser Issues**: Clear cache or try a different browser if the web interface doesn't load properly.

