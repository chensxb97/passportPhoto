from flask import Flask, request, render_template, send_file, send_from_directory
import tempfile
import cv2
import numpy as np
import os

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
    
    return resized

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    filename_with_extension = file.filename
    filename, extension = os.path.splitext(filename_with_extension)
    
    processed_img = process_image(file)
    
    # Send the image to client for download
    if processed_img is not None:
        with tempfile.NamedTemporaryFile(delete=False, suffix='.jpg') as temp_file:
            root = os.getcwd()
            filesDir = root + '/files'
            filePath = f'{filesDir}/{filename}_processed{extension}'
            cv2.imwrite(filePath, processed_img)
        return send_file(filePath, as_attachment=True)
    else:
        return 'Failed to process image. Image is either in an invalid format or image does not contain a face.', 400

if __name__ == '__main__':
    app.run(debug=True)
