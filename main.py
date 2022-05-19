from distutils.log import debug
from flask import *

app = Flask (__name__)
app.secret_key = "magdelinpai"


@app.get("/")
def home():
    return render_template("productos/index.html")


#Metodos Empresa
@app.get("/empresa-registro")
def empresaRegistro():
    return render_template("empresas/registro.html")


@app.get("/empresa-sesion")
def empresaSesion():
    return render_template("empresas/sesion.html")

#metodos producto

@app.get("/productos-empresa")
def productoEmpresas():
    return render_template("productos/productoEmpresas.html")

@app.get("/productos-registro")
def productoRegistro():
    return render_template("productos/productoRegistro.html")


@app.get("/productos-editar")
def productoEditar():
    return render_template("productos/productoEditar.html")


@app.get("/productos-eliminar")
def productoEliminar():
    print('eliminado productoo')
    return render_template("productos/productoRegistro.html")
    
app.run(debug=True)