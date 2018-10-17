from procesos import datos
usuario = "Joshell"
nombre_audio='{}'.format(nombre_audio)
formato='{}'.format(formato)
duracion='{}'.format(duracion)
frecuencia='{}'.format(frecuencia)
canal='{}'.format(canal)
ruta='{}'.format(ruta)


#Insertar datos ()
def insertar():
   	sql="INSERT INTO audio VALUES"
	sql+= "('" +usuario+"','" +nombre_audio+ "','" +formato+ "','" +duracion+ "','"+frecuencia+ "','"+capacidad+"','" +ruta+ "')"
	cur.execute(sql)
	
    

