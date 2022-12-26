#app.py
from flask import Flask, flash, request, redirect, url_for, render_template
import urllib.request
import os
from werkzeug.utils import secure_filename
from PIL import Image, ImageDraw
import cv2
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from collections import Counter
from skimage.color import rgb2lab, deltaE_cie76
from helper_function import detect_image
from color_detect import color_model
 
app = Flask(__name__)


UPLOAD_FOLDER = 'static/files/'
DETECTED_FOLDER = 'static/detect/exp/'
CROPPED_FOLDER = 'crop/'
PIECHARTS_FOLDER = "pie_charts/"
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
 
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['DETECTED_FOLDER'] = DETECTED_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
     

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload_picture')
def upload_picture():
    return render_template('uploadpic.html')
 
@app.route("/upload_picture", methods = ['POST'])
def upload_image():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)

    file = request.files['file']
    print(file.filename)

    if file.filename == '':
        flash('No image selected for uploading')
        return redirect(request.url)

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        print('upload_image filename: ' + filename)
        detect_image(filename)
        global hex_colors_all
        hex_colors_all = color_model()
        print(hex_colors_all)
        flash('Image successfully uploaded and displayed below with detections')

        return render_template('uploadpic.html', filename=filename)
    else:
        flash('Allowed image types are - png, jpg, jpeg')
        return redirect(request.url)
 
@app.route('/display/<filename>')
def display_image(filename):
    #print('display_image filename: ' + filename)
    return redirect(url_for('static', filename='detect/exp/' + filename), code=301)

 
@app.route('/results')
def results():
    global hex_colors_all
    result_colors = [[col[1:] for col in col_sec.split(', ')]for col_sec in hex_colors_all]
    print(hex_colors_all)
    return render_template('results.html', hex_colors_all = result_colors)

if __name__ == "__main__":
    app.run(debug=True, port=3001) 
    