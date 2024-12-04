from flask import Flask, request, render_template, jsonify, send_file, url_for
from spoofer.spoofer_core import ImageHashSpoofer
from spoofer.validators import is_valid_prefix, allowed_file
from spoofer import log_message
import os
import io
import hashlib

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # Limit file size to 16MB
app.static_folder = 'static'

# Ensure upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

def calculate_hash(image_data: bytes) -> str:
    """Calculate the SHA-512 hash of the image data."""
    hash_obj = hashlib.sha512()
    hash_obj.update(image_data)
    return hash_obj.hexdigest()

@app.route('/')
def index():
    """Render the main upload page."""
    return render_template('index.html')

@app.route('/spoof', methods=['POST'])
def spoof_image():
    """Handle image spoofing requests."""
    target_prefix = request.form.get('target_prefix')
    uploaded_file = request.files.get('image')

    # Validate inputs
    if not target_prefix or not is_valid_prefix(target_prefix):
        return render_template(
            'index.html',
            error="Invalid target prefix. Must be a valid hex string."
        )

    if not uploaded_file or not allowed_file(uploaded_file.filename):
        return render_template(
            'index.html',
            error="Invalid file type. Only PNG, JPG, and JPEG are allowed."
        )

    try:
        # Read the uploaded image
        image_data = uploaded_file.read()
        spoofer = ImageHashSpoofer(target_prefix)

        log_message("Starting spoofing process.")
        altered_image = spoofer.create_image_with_target_hash(image_data)

        if altered_image:
            # Calculate hash of spoofed image
            altered_image.seek(0)  # Reset file pointer before reading for hash
            spoofed_hash = calculate_hash(altered_image.read())
            altered_image.seek(0)  # Reset again for saving the image

            # Log hash and prefix to debug
            log_message(f"Target Prefix: {target_prefix}")
            log_message(f"Generated Spoofed Hash: {spoofed_hash}")

            # Remove the '0x' prefix if present before comparison
            if target_prefix.startswith("0x"):
                target_prefix = target_prefix[2:]

            # Verify prefix match (compare after removing '0x')
            matches_prefix = spoofed_hash.startswith(target_prefix.lower())
            log_message(f"Matches Prefix: {matches_prefix}")

            # Save the spoofed image for download
            output_filename = 'spoofed_image.png'
            output_path = os.path.join(app.config['UPLOAD_FOLDER'], output_filename)
            altered_image.seek(0)
            with open(output_path, 'wb') as f:
                f.write(altered_image.read())

            # Redirect to result page
            return render_template(
                'result.html',
                hash=spoofed_hash,
                matches_prefix=matches_prefix,
                target_prefix=target_prefix,
                download_path=url_for('download_file', filename=output_filename)
            )
        else:
            log_message("Failed to generate image with target hash within limits.", level="error")
            return render_template(
                'index.html',
                error="Unable to spoof the image within the iteration limit."
            )

    except Exception as e:
        log_message(f"Error during spoofing: {str(e)}", level="error")
        return render_template(
            'index.html',
            error="An error occurred during the spoofing process. Please try again."
        )

@app.route('/download/<filename>')
def download_file(filename):
    return send_file(os.path.join(app.config['UPLOAD_FOLDER'], filename), as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
