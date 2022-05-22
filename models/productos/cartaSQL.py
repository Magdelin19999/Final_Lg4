from config import dataBase
from controllers.imagenes import binary 

DB = dataBase.DB
DB.autocommit = True

whereAllActivos = "WHERE  prod.`estado`=1  ORDER BY fecha DESC;"
selectActivos ="""
SELECT
  prod.`id` AS producto_id,
  prod.`id_usuario` AS empresa_id,
  categoria.`descripcion`AS categoria,
  prod.`nombre`,
  prod.`descripcion`,
  prod.`precio`,
  prod.`imagen`,
  prod.`fecha`,
  `empresa`.`nombreEmpresa`,
  empresa.`direccionEmpresa`,
  `empresa`.`logoEmpresa`
FROM
  `cartavirtual`.`productos` AS prod
INNER JOIN `categoria`
ON `categoria`.`id`=prod.`id_categoria`
INNER JOIN `usuarios` AS empresa
ON  empresa.`id`=prod.`id_usuario`
"""
 
def productosAll():
    productos = []
    SQL = f'{selectActivos} {whereAllActivos}'
    cursor = DB.cursor(dictionary=True)
    cursor.execute(SQL)
    productos = cursor.fetchall()
    cursor.close()
    
    return productos; 
  
def productoID(id):
    producto = []
    SQL = f'{selectActivos} WHERE prod.`estado`=1 AND prod.`id`={id}'
    cursor = DB.cursor(dictionary=True)
    #print(SQL)
    cursor.execute(SQL)
    producto = cursor.fetchone()
    cursor.close()
    
    return producto; 
    
    print(id)