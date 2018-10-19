import MySQLdb
from crud import insertar

db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="miguel221",  # your password
                     db="audio")        # name of the data base
 
cur = db.cursor()

sql=("CREATE TABLE audio( usuario varchar(20) ,nombre_audio varchar(50) not null, formato varchar(20)not null, duracion varchar(20) not null,frecuencia varchar(20) not null, canal varchar(20)not null, ruta varchar(200)not null)")
cur.execute(sql)

insertar()

db.close()
