from flask import *
from controllers.empresas import manipulacionUsuarios as USUARIOS
from controllers.productos import manipulacionProductos as PRODUCTOS, cartaManipulacion as carta


app = Flask (__name__)
app.secret_key = "magdelinpai"

''' cambiar hasta que ya este lo de validacion de login '''
id_usuario = 42
id_categoria=1

@app.get("/")
def home():
    productos = carta.getAllProducts()
    return render_template("productos/index.html",empresas=productos)


#Metodos Empresa
@app.route("/empresa-registro", methods=['GET', 'POST'])
def empresaRegistro():
    if request.method == 'POST':
        logoEmpresa = request.files['logoEmpresa']
        flash('Usuario registrado.... Revisa tu correo Para completar el registro')
        print(request.form,logoEmpresa)
        
        USUARIOS.datosFormulario(request.form, logoEmpresa)
    return render_template("empresas/registro.html")

@app.get("/activar-empresa/<token>")
def activarEmpresa(token):
    
    resultadiActivacion =  USUARIOS.returnID(token)
    print(resultadiActivacion)
    id = resultadiActivacion["id"]
    print('\n',id)
    if resultadiActivacion['resultado']:
        result = USUARIOS.activacion(id)
        flash(result['mensaje'],result['category'])
        if result['estado']:
            return render_template('empresas/sesion.html')
        else:
            return render_template('empresas/resgistro.html') 
    else:
        flash("Finalizo tiempo de activacion","warning")
        #USUARIOS.eliminarNoActivo(id)
        return redirect(url_for("home"))
        

@app.get("/empresa-editar")
def empresaEditar():
    return render_template("empresas/editar.html")


#metodos sesion
@app.get("/empresa-logout")
def empresaFinSesion():
    print('\n\n\tFinal sesion')
    return redirect(url_for("home"))

@app.get("/empresa-sesion")
def empresaSesion():
    titulo='Please sign in'
    return render_template("empresas/sesion.html",titulo=titulo)

@app.get("/empresa-cambio-pass")
def empresaCambioPass():
    titulo='Cambio de Contraseña'
    return render_template("empresas/sesion.html",titulo=titulo)
#metodos producto

@app.get("/productos-empresa")
def productoEmpresas():
    return render_template("productos/productoEmpresas.html")

@app.route("/productos-registro", methods=['GET', 'POST'])
def productoRegistro():
    if request.method == 'POST':
        imgProducto = request.files['imgProducto']
        print(request.form)
        PRODUCTOS.datosFormulario(request.form, imgProducto)
    return render_template("productos/productoRegistro.html")


@app.get("/productos-editar")
def productoEditar():
    return render_template("productos/productoEditar.html")


@app.get("/productos-eliminar")
def productoEliminar():
    print('eliminado productoo')
    return render_template("productos/productoRegistro.html")
    
app.run(debug=True)