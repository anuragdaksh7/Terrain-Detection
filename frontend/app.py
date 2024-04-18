from flask import Flask, request, jsonify, render_template
from PIL import Image  # Or your preferred image processing library
import numpy as np

from imageProcess import *

app = Flask(__name__)

@app.route('/process-image', methods=['POST'])
def process_image():
    if 'image_file' not in request.files:
        return jsonify({'error': 'No image file provided'}), 400

    image_file = request.files['image_file']

    # Image Processing (Example: Grayscale Conversion)
    try:
        image = Image.open(image_file).convert('L')
        image.save('processed_image.jpg')  # Adjust as needed
        return (jsonify({'message': processImage(image)}), 200)
    except Exception as e:
        return (jsonify({'error': 'Image processing error'}), 500)

@app.route('/')
def index():
    return render_template('index.html') 

if __name__ == '__main__':
    app.run(debug=True) 
