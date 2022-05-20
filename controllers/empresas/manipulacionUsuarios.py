from hashlib import md5


from models.empresas import setenciasSQLUsusarios as SQL
from models.mensaje import mensaje as sendMensaje

from controllers.token import generar
from controllers.imagenes import path,binary


def datosFormulario(form,logoEmpresa):

    nombreEmpresa, descEmpresa, celularEmpresa, direccionEmpresa, correo, contrasenia = form.values()
    contrasenia = encriptarContraseña(contrasenia)
    
    logoEmpresa= path.imagenPath(logoEmpresa,'user')
    
    resultado = SQL.insertUsuario(nombreEmpresa, descEmpresa, celularEmpresa,
                                  direccionEmpresa, correo, contrasenia, logoEmpresa)

    if (isinstance(resultado, int) == True):
        keyToken = generar.generarKey(resultado)
        sendMensaje.mensaje(correo, resultado, keyToken)

# token 
def returnID(token):
    return generar.returnID(token)

def tokenCambioContra(id):
    keyToken = generar.generarKey(id)
    
# sql models
def activacion(id):
    return SQL.obtenerDBID(id)

def eliminarNoActivo(id):
    SQL.eliminarID(id)
# sesion usuario
def inicioSesion(correo, contrasenia):
    return (SQL.obtenerEmpresa(correo, encriptarContraseña(contrasenia)))

def cerrarSesion():
    SQL.cerrarSesion()   

# helpers

def encriptarContraseña(contrasenia):
    return md5(contrasenia.encode("utf-8")).hexdigest()




