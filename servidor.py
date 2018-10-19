#Import
import os
import wave
import contextlib
import soundfile as sf
from flask import Flask, flash, request, redirect
from werkzeug.utils import secure_filename
from pydub import AudioSegment
from procesos import controlador
     
#Destination of the file
UPLOAD_FOLDER = '/home/miqueel/Escritorio/Nuevo/'
#Format allowed
ALLOWED_EXTENSIONS = set(['mp3'])

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
     
def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
     
@app.route('/work', methods=['GET', 'POST'])
#Function upload_file
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            flash('file {} saved'.format(file.filename))
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    controlador()
    return '''
    gracias
    '''


#Function main
if __name__ == '__main__':
    	app.run(debug=True)
