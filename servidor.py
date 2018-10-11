import os
import wave
import contextlib
import soundfile as sf
from flask import Flask, flash, request, redirect
from werkzeug.utils import secure_filename
from pydub import AudioSegment
     
UPLOAD_FOLDER = '/home/miqueel/Escritorio/Nuevo/'
ALLOWED_EXTENSIONS = set(['mp3','wav', 'mpeg'])

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
     
def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
     
@app.route('/', methods=['GET', 'POST'])
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
	    for archivo in os.listdir(UPLOAD_FOLDER):
			name_file=archivo.split('.')
			print(name_file)
			if(name_file[1]=='mp3'):
				sound = AudioSegment.from_mp3(UPLOAD_FOLDER+archivo)
				sound.export(UPLOAD_FOLDER+name_file[0]+".wav", format="wav")
				return redirect('/velocidad')        
				#return ("Satisfactorio")
        	

    return '''
    
    '''


@app.route('/velocidad')
def velocidad():
	for archivo in os.listdir(UPLOAD_FOLDER):
		name_file=archivo.split('.')
		if (name_file[1]=='wav'):
			CHANNELS = 1
			swidth = 4
			Change_RATE = 0.5
			spf = wave.open(archivo, 'rb')
			RATE=spf.getframerate()
			signal = spf.readframes(-1)
			wf = wave.open(name_file[0]+'_velocidad.---wav', 'wb')
			wf.setnchannels(CHANNELS)
			wf.setsampwidth(swidth)
			wf.setframerate(RATE*Change_RATE)
			wf.writeframes(signal)
			wf.close()
			sound1=AudioSegment.from_file(UPLOAD_FOLDER+archivo)
			sound2=AudioSegment.from_file("/home/miqueel/Escritorio/onda.wav")
			combined=sound1.overlay(sound2)
			combined.export(name_file[0]+"_combine.---wav", format='wav')


	return redirect('/particion')

@app.route('/particion')
def particion():
	for archivo in os.listdir(UPLOAD_FOLDER):
		name_file=archivo.split('.')
		print(name_file)
		if(name_file[1]=='wav'):
			f=sf.SoundFile(archivo)
			time = 30000
			j=1
			with contextlib.closing(wave.open(UPLOAD_FOLDER+archivo,'r')) as f:
	    			frames = f.getnframes()
	    			rate = f.getframerate()
	    			duration = int((frames / float(rate))*1000)
				for i in range (0,duration,time):
					newAudio = AudioSegment.from_wav(archivo)
					newAudio = newAudio[i:i+30000]
					newAudio.export(name_file[0]+'_'+str(j)+".---wav", format="wav")
					j=j+1
	#return redirect('/velocidad')
	return '''
	Transformacion Satisfactoria'''

if __name__ == '__main__':
    	app.run(debug=True)