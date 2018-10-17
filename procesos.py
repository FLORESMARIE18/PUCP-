import os
import wave
import contextlib
import soundfile as sf
from flask import Flask, flash, request, redirect
from werkzeug.utils import secure_filename
from pydub import AudioSegment
UPLOAD_FOLDER = '/home/miqueel/Escritorio/Nuevo/'

def controlador():
	datos()
	cambio()
	velocidad()
	ruido()
	particion()

def datos():
	for archivo in os.listdir(UPLOAD_FOLDER):
			name_file=archivo.split('.')
			if(name_file[1]=='mp3' or name_file[1]=='wav'):
				sound = AudioSegment.from_mp3(archivo)
				nombre_audio=archivo
				formato =name_file[1]
				duracion= sound.duration_seconds
				frecuencia = sound.frame_rate
				channels = sound.channels
				if channels==2:
					chaneel='estereo'
				if channels ==1:
					chaneel='mono'
				canal=chaneel
				ruta=UPLOAD_FOLDER+archivo




def cambio():
	for archivo in os.listdir(UPLOAD_FOLDER):
			name_file=archivo.split('.')
			if(name_file[1]=='mp3'):
				sound = AudioSegment.from_mp3(UPLOAD_FOLDER+archivo)
				sound.export(UPLOAD_FOLDER+name_file[0]+".wav", format="wav")


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

def ruido():
	for archivo in os.listdir(UPLOAD_FOLDER):
		name_file=archivo.split('.')
		if(name_file[1]=='wav'):
			sound1=AudioSegment.from_file(UPLOAD_FOLDER+archivo)
			sound2=AudioSegment.from_file("/home/miqueel/Escritorio/onda.wav")
			combined=sound1.overlay(sound2)
			combined.export(name_file[0]+"_combine.---wav", format='wav')

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
