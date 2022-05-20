from hashlib import md5


from models.productos import sentenciasSQLProductos as SQL

from controllers.imagenes import path,binary

id_usuario = 42
id_categoria=1

def datosFormulario(form,imgProducto):

    nombre, descripcion,precio,estado = form.values()
    print(nombre)
    imgProducto= path.imagenPath(imgProducto,'temp')
    fecha = path.TimeNow()
    SQL.registroProducto(
            id_usuario, id_categoria, nombre, descripcion, 
            precio,     estado,     imgProducto, fecha)
    
    #resultado = SQL.insertUsuario()



# sql models

# sesion usuario

# helpers





