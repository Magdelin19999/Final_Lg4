from flask import session
from config import dataBase
from controllers.imagenes import binary 

DB = dataBase.DB
DB.autocommit = True


def insertUsuario(
    nombreEmpresa, descEmpresa, celularEmpresa, 
    direccionEmpresa, correo, contrasenia,logoEmpresa
):
    cursor = DB.cursor()
    SQL = """INSERT INTO usuarios(  `nombreEmpresa`,`descEmpresa`,
                                    `celularEmpresa`, `direccionEmpresa`,
                                    `correo`, `contrasenia`,
                                    `logoEmpresa`) 
	        VALUES(%s,%s,%s,%s,%s,%s,%s);"""
    #convertir a binario el  logoEmpresa
    logoEmpresa= binary.converBlod(logoEmpresa)
    AGRS=(nombreEmpresa, descEmpresa, celularEmpresa, direccionEmpresa, correo, contrasenia,logoEmpresa)
    
    cursor.execute(SQL, AGRS)
    idultimo = cursor.lastrowid
    cursor.close()
    
    return idultimo

def usuarios():
    empresa = []
    cursor = DB.cursor(dictionary=True)
    cursor.execute(f"""SELECT * FROM usuarios;""")
    empresa = cursor.fetchall()
    cursor.close()
    print(len(empresa))
    
def obtenerDBID(id):
    empresa = []
    cursor = DB.cursor(dictionary=True)
    cursor.execute(f"""SELECT * FROM usuarios WHERE id={id};""")
    empresa = cursor.fetchone()
    cursor.close()
    if empresa:
        print(f"tamaño diccionario {len(empresa)}")
        activarID(empresa["id"])
        return {'estado':True, 'mensaje':f'Registro finalizado, inicia sesion  :)',"category": "success"}

    return {'estado':False, 'mensaje':f'Error al activar Cuenta :(' ,"category": "warning",}

def activarID(id):
    print("ativando id", id)
    cursor = DB.cursor()
    cursor.execute(f"UPDATE usuarios SET estado = 1 WHERE id = {id}")
    cursor.close()
    
def eliminarID(id):
    cursor = DB.cursor()
    cursor.execute(f"""DELETE FROM `usuarios` WHERE `id` = {id};""")
    cursor.close()
    
def obtenerEmpresa(correo, contrasenia):
    #print(correo,contrasenia)
    empresa =[]
    cursor = DB.cursor(dictionary=True)
    cursor.execute(
        f"""SELECT * FROM usuarios   
                   WHERE correo = '{correo}' AND contrasenia = '{contrasenia}' ;"""
    )
    empresa = cursor.fetchone()
    cursor.close()
    if empresa:
        nuevaSesion(empresa["id"],empresa["nombreEmpresa"],empresa['logoEmpresa'])
        return {'estado':True, 'mensaje':f'Bienvenido {empresa["nombreEmpresa"]}' }

    return {'estado':False, 'mensaje':'Error de inicio de sesion :(' }

def nuevaSesion(id_empresa, nombreEmpresa,logoEmpresa):
    session["loggedin"] = True
    session["id"] = id_empresa
    session["usuario"] = nombreEmpresa
    session["logoEmpresa"] = binary.converImagen(logoEmpresa,nombreEmpresa,'user')
        
def cerrarSesion():
    session.pop("loggedin", None)
    session.pop("id", None)
    session.pop("usuario", None)
    session.pop("logoEmpresa", None)
    
