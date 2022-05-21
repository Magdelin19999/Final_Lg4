import base64
from PIL import Image
import io 
import os

''' '''
def converBlod(imagen):
    print('\n\n\n\n\n\n\n\t',imagen)
    file = open(imagen,'rb').read()
    # We must encode the file to get base64 string
    os.remove(imagen)
    #imagen.remove(imagen)
    file = base64.b64encode(file)
    return file

def converImagen(imagenBi, nombre,dir):
    binary_data = base64.b64decode(imagenBi)
    imagenBi = Image.open(io.BytesIO(binary_data))
    #print(imagenBi.format)
    # Display the image
    #imagenBi.show()
    nombre= nombre.replace(" ", "")
    path = f'static/img/{dir}/{nombre}.{imagenBi.format}'
    #print(path)
    imagenBi.save(path)
    #path = path.replace("static/", "")
    
    return path
