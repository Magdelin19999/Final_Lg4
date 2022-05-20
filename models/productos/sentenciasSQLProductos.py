from config import dataBase
from controllers.imagenes import binary 

DB = dataBase.DB
DB.autocommit = True

def registroProducto(id_usuario, id_categoria, nombre, 
                     descripcion, precio, estado, imgProducto, fecha):
    SQL = """INSERT INTO `cartavirtual`.`productos` (
        `id_usuario`, `id_categoria`, `nombre`, `descripcion`, 
        `precio`,      `estado`,        `imagen`, `fecha` 
        ) VALUES (  %s, %s, %s, %s, 
                    %s, %s, %s,%s);"""
    #convertir a binario el  logoEmpresa
    imagen= binary.converBlod(imgProducto)
    AGRS=(  id_usuario, id_categoria, nombre, descripcion, 
            precio,     estado,     imagen, fecha)
    cursor = DB.cursor()
    print(SQL,AGRS)
    cursor.execute(SQL, AGRS)
    cursor.close()