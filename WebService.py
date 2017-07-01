import usuarios
from flask import Flask, request

app = Flask("Server")

@app.route('/nuevoUsuario', methods=['POST'])
def nuevoUsuario():
    usuario = str(request.form['usuario'])
    contrasena = str(request.form['contrasena'])
    conexion = bool(request.form['conexion'])
    if usuarios.arbol.crearNodo(usuario, contrasena, conexion):
        usuarios.arbol.grafica = "digraph g{ "
        usuarios.arbol.preOrden(usuarios.arbol.raiz)
        usuarios.arbol.grafica = usuarios.arbol.grafica + "}"
        usuarios.arbol.crearArch()
        usuarios.arbol.ejecutar()
        return "True"
    return "False"

@app.route('/Login', methods=['POST'])
def login():
    raiz = usuarios.arbol.raiz
    usuario = str(request.form['usuario'])
    contrasena = str(request.form['contrasena'])
    if usuarios.arbol.Login(raiz, usuario, contrasena):
        return "True"
    return "False"

@app.route('/leerUsuarios', methods = ['POST'])
def leerUsuarios():
    path = str(request.form['path'])
    if usuarios.arbol.leerArchivoUsuarios(path):
        return "True"
    return "False"

if __name__ == '__main__':
    app.run()
