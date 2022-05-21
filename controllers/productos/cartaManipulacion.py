from models.productos import cartaSQL

from controllers.imagenes import binary,path

def getAllProducts():
    productos = cartaSQL.productosAll()
    if(len(productos)>0):
        return pathToImagen(productos)
        
def pathToImagen(productos):
    ## eliminar archivos carpeta Temp
    path.eliminarTemp()

    empresas= nombresEmpresas(productos)
  
    for producto in productos:
        #print(producto['nombre'])
        filename = f'{path.TimeNow()}-{producto["nombre"]}'
        filename= filename.replace(" ", "_")
        filename= filename.replace(":", "_")
        filename= filename.replace("-", "_")
        imagen = binary.converImagen(imagenBi=producto['imagen'],nombre=filename,dir='temp')
        producto['imagen']=imagen
        
    print('\n\n------')

    for emp in empresas:
        for producto in productos:
            aux = {
                'producto_id' : producto['producto_id'],
                'imagen' : producto['imagen'],
                'nombre' : producto['nombre'],
                'descripcion' : producto['descripcion'],
                'categoria' : producto['categoria'],
                'precio' : producto['precio'],
                'fecha' : producto['fecha'],
            }
            if(emp['nombreEmpresa']==producto['nombreEmpresa']):
                print('recorriendo:',producto['producto_id'],' ', producto['nombre'])
                isRegistrado(emp['productos'],producto['producto_id'])
                emp['productos'].append(aux)
                
                
    print('\n\n------')
             
    return empresas

def isRegistrado(productos,nuevo):
    resul = False
    for prod in productos:
        if(prod['producto_id']==nuevo):
            print('Ya se registro')
            resul = True
    return resul
            
            
def nombresEmpresas(productos):
    nombres =[]
    empresas=[]
    for item in productos:
        nombres.append(item['nombreEmpresa'])
    for nm in nombres:
        if(nombres.count(nm)>1):
            nombres.remove(nm)
            
    for nm in nombres:
        for empresa in productos:
            filename = f'{path.TimeNow()}-{empresa["nombreEmpresa"]}'
            filename= filename.replace(" ", "_")
            filename= filename.replace(":", "_")
            filename= filename.replace("-", "_")
            imagen = binary.converImagen(imagenBi=empresa['logoEmpresa'],nombre=filename,dir='temp')
            aux={
                    'nombreEmpresa' : empresa['nombreEmpresa'],
                    'direccionEmpresa' : empresa['direccionEmpresa'],
                    'logoEmpresa' : imagen,
                    'productos':[]
                }
            if(len(empresas)>0):
                for emp in empresas:
                    if(emp['nombreEmpresa']!=empresa['nombreEmpresa']):
                        empresas.append(aux)
                        
            else:
                empresas.append(aux)                    
    #print(empresas)

    return empresas

