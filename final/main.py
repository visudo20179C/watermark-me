#!/usr/bin/python3
import os, glob
from flask import Flask, flash, request, redirect, url_for, send_from_directory
from PIL import Image, ImageDraw, ImageFont

ALLOWED_EXTENSIONS = {'.png'}
UPLOAD_FOLDER = '/root/bin/IT3038C/IT30308C/projects/final/img/'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def upload_file():
  if request.method == 'POST':
    # check if the post request has the file part
    if 'file' not in request.files:
      flash('No file part')
      return redirect(request.url)
    file = request.files['file']
    marktext = request.form['text']
    # if user does not select file, browser also
    # submit an empty part without filename
    if file.filename == '':
      flash('No selected file')
      return redirect(request.url)
    if file and marktext:
      filename = file.filename
      newfile = process_file(file, marktext)
      newfile.save(os.path.join(app.config['UPLOAD_FOLDER'], filename)) 
      return redirect(url_for('uploaded_file', filename=file.filename))
  return '''
  <!doctype html>
  <title>Watermarking App</title>
  <h1>Upload image file</h1>
  <form method=post enctype=multipart/form-data>
    <input type=file name=file>
    <input type=text name=text>
    <input type=submit value=Upload>
  </form>
  '''

@app.route('/file-dl/<filename>')
def uploaded_file(filename):
  return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

def process_file(file, marktext):
  img = Image.open(file)
  text = marktext
  width, height = img.size
  draw = ImageDraw.Draw(img)
  font = ImageFont.truetype('fonts/ostrich-black-webfont.ttf', 12)
  twidth, theight = draw.textsize(text, font)
  margin = 5
  x = width - twidth - margin
  y = height - theight - margin
  draw.text((x,y), text, font=font)
  return img

def allowed_file(filename):
  return '.' in filename and \
   filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

