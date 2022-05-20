from models.productos import cartaSQL

from controllers.imagenes import binary,path

def getAllProducts():
    productos = cartaSQL.productosAll()
    if(len(productos)>0):
        return pathToImagen(productos)
        
def pathToImagen(productos):
    print(type(productos))
    producPath = [{'empresa':'','productos':[]}]
    empresas= nombresEmpresas(productos)
    for producto in productos:
        filename = f'{path.TimeNow()}-{producto["nombre"]}'
        filename= filename.replace(" ", "_")
        filename= filename.replace(":", "_")
        filename= filename.replace("-", "_")
        imagen = binary.converImagen(imagenBi=producto['imagen'],nombre=filename,dir='temp')
        producto['imagen']=imagen
        
    # agrupar por empresas 
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
                emp['productos'].append(aux)
    #print(empresas)     
    
    for producto in empresas:
        for detalle in producto['productos']:
            print(detalle)
            
    return empresas


 

def nombresEmpresas(productos):
    nombres =[]
    empresas = []
    
    for item in productos:
        nombres.append(item['nombreEmpresa'])
    for nm in nombres:
        if(nombres.count(nm)>1):
            nombres.remove(nm)
    for nm in nombres:
        for empresa in productos:
            if(nm==empresa['nombreEmpresa']):
                filename = f'{path.TimeNow()}-{empresa["nombreEmpresa"]}'
                filename= filename.replace(" ", "_")
                filename= filename.replace(":", "_")
                filename= filename.replace("-", "_")
        
                imagen = binary.converImagen(imagenBi=empresa['logoEmpresa'],nombre=filename,dir='user')
                
                empresas.append({
                    'nombreEmpresa' : empresa['nombreEmpresa'],
                    'direccionEmpresa' : empresa['direccionEmpresa'],
                    'logoEmpresa' : imagen,
                    'productos':[]
                })
    return empresas

