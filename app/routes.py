# SoundArt
# Copyright 2018 pauldamora.com All rights reserved
#
# Authors: Paul D'Amora
#
# Description: Defines the user's view
from app import app
from flask import request, url_for, render_template, jsonify,\
    send_from_directory
from app.wave import convert_to_png


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/_upload', methods=['POST'])
def upload_file():
    filename, error = None, None

    if request.method == 'POST':
        # Check if the post request has the file part
        if 'file' not in request.files:
            error = 'Error: No file part received by server. Please try again.'

        file = request.files['file']

        # If user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            error = 'Error: No file selected. Please try again.'

        # If the file is good, save it
        if file:
            filename = convert_to_png(file)

    rendered = render_template('download.html', filename=filename)
    return jsonify(content=rendered, filename=filename,
                   success=error is None, error=error)


@app.route('/uploads/<filename>')
def send_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
