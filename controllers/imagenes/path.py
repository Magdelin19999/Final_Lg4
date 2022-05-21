import glob, os
from datetime import datetime
from datetime import date

def imagenPath(imagen,dir):
    nombre_imagen = (imagen.filename).replace(" ", "")
    path = f'static/img/{dir}/{nombre_imagen}'
    #print('\n\n\n\n\n',path)
    imagen.save(path)
    return path

def TimeNow():
    today = date.today()
    now = datetime.now()
    nombreTime = f'{str(today)} {str(now.hour)}:{str(now.minute)}:{str(now.second)}'
    #print('\n\n\n\t2022-05-20 07:45:20\n\t',nombreTime)
    
    return nombreTime

def eliminarTemp():
     files = glob.glob('static/img/temp/*') 
     print('Eliminando ando')
     for f in files: 
        os.remove(f)

