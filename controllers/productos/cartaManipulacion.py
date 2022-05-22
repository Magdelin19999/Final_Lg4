from flask import jsonify
from models.productos import cartaSQL

from controllers.imagenes import binary,path

def getAllProducts():
    productos = cartaSQL.productosAll()
    #validar si existe carpeta img
    path.crearCarppetas('static/img/')
    if(len(productos)>0):
        return pathToImagen(productos)
    return [] 

def obtenerId(id):
    print(id)
    producto = cartaSQL.productoID(id)
    if(producto):
        producto['logoEmpresa']=retunPathImg(nombre=producto["nombreEmpresa"],binario=producto['logoEmpresa'],dir='temp')
        producto['imagen']=retunPathImg(nombre=producto["nombre"],binario=producto['imagen'],dir='temp')
        

        return{
            'res':'true',
            'response':producto
        }
    else:
        return {'res':'false','response':''}
    

#helpers  
def pathToImagen(productos):
    ## eliminar archivos carpeta Temp
    path.eliminarTemp()
    empresas= nombresEmpresas(productos)

    for emp in empresas:
        for producto in productos:
            imgagen_prod = retunPathImg(nombre=producto["nombre"],binario=producto['imagen'],dir='temp')
            aux = {
                'producto_id' : producto['producto_id'],
                'imagen' : imgagen_prod,
                'nombre' : producto['nombre'],
                'descripcion' : producto['descripcion'],
                'categoria' : producto['categoria'],
                'precio' : producto['precio'],
                'fecha' : producto['fecha'],
            }
            if(emp['nombreEmpresa']==producto['nombreEmpresa']):
                result = isRegistrado(emp['productos'],producto['producto_id'],'producto_id')
                if(result==False):
                    emp['productos'].append(aux)
    
    return empresas

def isRegistrado(datos,nuevo,campo):
    resul = False
    for dt in datos:
        if(dt[campo]==nuevo):
            print('Ya se registro')
            resul = True
    return resul

def retunPathImg(nombre, binario,dir):
    filename = f'{path.TimeNow()}-{nombre}'
    filename= filename.replace(" ", "_")
    filename= filename.replace(":", "_")
    filename= filename.replace("-", "_")  
    return binary.converImagen(imagenBi=binario,nombre=filename,dir=dir)   
               
def nombresEmpresas(productos):
    nombres =[]
    result = []
    # agregando nombres de empresa
    for item in productos:
        nombres.append(item['nombreEmpresa'])
    # eliminando nombres de empresas repetidos
    
    for nm in nombres:
        if(nombres.count(nm)>1):
            nombres.remove(nm)
    
    for item in nombres:
        for empresa in productos:
           
            registrada = isRegistrado(result, empresa['nombreEmpresa'],'nombreEmpresa')
            if((item==empresa["nombreEmpresa"]) & ( registrada== False)): 
              
                imagen= retunPathImg(nombre=empresa["nombreEmpresa"],binario=empresa['logoEmpresa'],dir='temp')
                
                aux={
                        'nombreEmpresa' : empresa['nombreEmpresa'],
                        'direccionEmpresa' : empresa['direccionEmpresa'],
                        'logoEmpresa' : imagen,
                        'productos':[]
                    } 
                result.append(aux)
    print('\n\n------')
    print(result)
    print('\n\n------')
   

    return result

