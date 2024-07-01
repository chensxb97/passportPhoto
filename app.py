from flask import Flask, request, render_template, send_file
from rembg import remove 
from PIL import Image
import tempfile
import cv2
import numpy as np
import os
import io

app = Flask(__name__)

def process_image(file):
    # Load image
    img = cv2.imdecode(np.frombuffer(file.read(), np.uint8), cv2.IMREAD_COLOR)
    
    # Resize image according to ICA standards
    new_width = 400
    new_height = 514
    resized = cv2.resize(img, (new_width, new_height))  # 400 x 514 pixels
    
    # Perform face detection
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    # Check if there is only 1 face
    if len(faces) != 1:
        return None

    # Remove background
    output = remove(resized, bgcolor=(255, 255, 255, 255))
    return output

def send_image(processed, name, extension):
    img_buffer = io.BytesIO()
    success, encoding = cv2.imencode(extension, processed)
    if not success:
        raise ValueError("Image encoding failed")
    
    img_buffer.write(encoding)
    img_buffer.seek(0)

    return send_file(img_buffer, mimetype=f'image/{extension.lstrip(".")}', as_attachment=True, download_name=f'{name}_resized{extension}')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return 'No file uploaded', 400
    
    file = request.files['file']
    if file.filename == '':
        return 'No file selected', 400
    
    name, extension = os.path.splitext(file.filename)

    if file:
        processed = process_image(file)

    if processed is None:
        return 'Process failed. Image is either in an invalid format or does not contain a face.', 400
    
    # Send the image back to client for download
    return send_image(processed, name, extension)

if __name__ == '__main__':
    app.run(debug=True)
