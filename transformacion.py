import os
import soundfile as sf
from pydub import AudioSegment
import wave
import contextlib

path = "/home/marie/Escritorio/prueba/"



def get_format(carpeta):
	print("entra")
	for archivo in os.listdir(carpeta):
		print(archivo)
		name_file = archivo.split('.')
		if(name_file[1]=="mp3"):
			sound = AudioSegment.from_mp3(path+archivo)
			sound.export(path+name_file[0]+".wav", format="wav")
			particion(carpeta)
		if(name_file[1]=="wav"):
			particion(carpeta)	
	velocidad(carpeta)

def velocidad(carpet):
	for archivo in os.listdir(carpet):
		name_file=archivo.split('.')
		print(archivo)
		if(name_file[1]=="wav"):
			CHANNELS = 1
			swidth = 4
			Change_RATE = 0.5
			spf = wave.open(archivo, 'rb')
			RATE=spf.getframerate()
			signal = spf.readframes(-1)
			wf = wave.open(name_file[0]+'_velocidad_'+'.wav', 'wb')
			wf.setnchannels(CHANNELS)
			wf.setsampwidth(swidth)
			wf.setframerate(RATE*Change_RATE)
			wf.writeframes(signal)
			wf.close()
			sound1 = AudioSegment.from_file(carpet+archivo)
			sound2 = AudioSegment.from_file("/home/marie/Escritorio/onda.wav")
			combined = sound1.overlay(sound2)
			combined.export(name_file[0]+"_combined.wav", format='wav')

def particion(ruta):
	for archiv in os.listdir(ruta):
		name_file=archiv.split('.')
		if(name_file[1]=="wav"):
			f=sf.SoundFile(archiv)
			time = 30000
			j=1
			with contextlib.closing(wave.open(ruta+archiv,'r')) as f:
	    			frames = f.getnframes()
	    			rate = f.getframerate()
	    			duration = int((frames / float(rate))*1000)
				for i in range (0,duration,time):
					newAudio = AudioSegment.from_wav(archiv)
					newAudio = newAudio[i:i+30000]
					newAudio.export(name_file[0]+'_'+str(j)+"'.wav'", format="wav")
					j=j+1

def main():
	get_format(path)


if __name__ == "__main__":
	main()
