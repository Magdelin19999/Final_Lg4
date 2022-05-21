from models.productos import cartaSQL

from controllers.imagenes import binary,path

def getAllProducts():
    productos = cartaSQL.productosAll()
    #validar si existe carpeta img
    path.crearCarppetas('static/img/')
    if(len(productos)>0):
        return pathToImagen(productos)
    return []   
def pathToImagen(productos):
    ## eliminar archivos carpeta Temp
    
    path.eliminarTemp()

    empresas= nombresEmpresas(productos)
    print(empresas)
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
                print(isRegistrado(emp['productos'],producto['producto_id']))
                result = isRegistrado(emp['productos'],producto['producto_id'])
                if(result==False):
                    print('nuevo')
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
            
def isRegistrada(empresas,nueva):
    result = False
    print('Nueva empresa: ', nueva )
    for emp in empresas:
        print('empresa registrada: ', emp['nombreEmpresa'] )
        
        if(nueva==emp['nombreEmpresa']):
            
            result = True
    return result     
              
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
           
            registrada = isRegistrada(result, empresa['nombreEmpresa'])
            if((item==empresa["nombreEmpresa"]) & ( registrada== False)): 
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
                result.append(aux)
    print('\n\n------')
    print(result)
    print('\n\n------')
    ''' 
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
                    if(empresa['nombreEmpresa'] not in emp['nombreEmpresa']):
                        empresas.append(aux)  
                        
            else:
                empresas.append(aux)  
 '''
    print('\n\n------')

    return result

