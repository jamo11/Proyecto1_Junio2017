# coding=utf-8
import juegos
from graphviz import Digraph

class nodoUsuario:
    def __init__(self, usuario, contrasena, conexion):
        self.lista = juegos.listaJuegos()
        self.usuario = usuario
        self.contrasena = contrasena
        self.conexion = conexion
        self.izquierda = None
        self.derecha = None

class arbolUsuarios:
    def __init__(self):
        self.raiz = None
        self.grafica = "digraph g {"

    def crearNodo(self, usuario, contrasena, conexion):
        aux = nodoUsuario(usuario, contrasena, conexion)
        if self.raiz is None:
            self.raiz = aux
        else:
            if self.insertarUsuario(self.raiz, aux) is not None:
                return True
            else:
                return False

    def insertarUsuario(self, raiz, nuevo):
        # si hay nodos en el árbol lo recorre
        bandera = 0
        while bandera == 0:
            usu1 = raiz.usuario
            usu2 = nuevo.usuario
            if usu1 > usu2:
                if raiz.izquierda is None:
                    raiz.izquierda = nuevo
                else:
                    raiz.izquierda = self.insertarUsuario(raiz.izquierda, nuevo)
                bandera = -1
            elif usu2 > usu1:
                if raiz.derecha is None:
                    raiz.derecha = nuevo
                else:
                    raiz.derecha = self.insertarUsuario(raiz.derecha, nuevo)
                bandera = -1
            elif usu1 == usu2:
                print "usuarios iguales"
                return None
            return raiz

    def preOrden(self, raiz):
        if raiz is not None:
            if raiz.izquierda is not None:
                self.grafica = self.grafica + '"' + str(raiz.usuario) + '"->"' + str(raiz.izquierda.usuario) + '"'
            if raiz.derecha is not None:
                self.grafica = self.grafica + '"' + str(raiz.usuario) + '"->"' + str(raiz.derecha.usuario) + '"'
            self.preOrden(raiz.izquierda)
            self.preOrden(raiz.derecha)

    def Login(self, raiz, usuario, contrasena):
        nodo = self.buscarUsuario(raiz, usuario)
        if nodo is None:
            return False
        else:
            if nodo.contrasena == contrasena:
                return True
            else:
                return False

    def buscarUsuario(self, raiz, usuario):
        if raiz.usuario == usuario:
            return raiz
        else:
            if raiz.usuario > usuario:
                if raiz.izquierda is None:
                    return None
                else:
                    return self.buscarUsuario(raiz.izquierda, usuario)
            else:
                if raiz.derecha is None:
                    return None
                else:
                    return self.buscarUsuario(raiz.derecha, usuario)

    def ejecutar(self):
        import os
        dotPath = "dot"
        fileInputPath = "arbol.txt"
        fileOutputPath = "arbol.png"
        tParam = " -Tpng "
        tOParam = " -o "
        tuple = (dotPath + tParam + fileInputPath + tOParam + fileOutputPath)
        os.system(tuple)

    def crearArch(self):
        arch = open('arbol.txt', 'w')
        arch.write(str(arbol.grafica))
        arch.close()

    def leerArchivoUsuarios(self, path):
        infile = open(path, 'r')
        content = infile.read()
        container = content.splitlines()
        for i in container:
            l = i.split(",")
            print str(l[0])
            print str(l[1])
            print str(l[2])
            if str(l[0]) != 'Usuario':
                print "_______________________________________"
                self.crearNodo(str(l[0]), str(l[1]),False)
        self.preOrden(self.raiz)
        self.grafica = self.grafica + "}"
        self.crearArch()
        self.ejecutar()
        return True

arbol = arbolUsuarios()
arbol.leerArchivoUsuarios("C:\Users\Andres\Desktop\UNIVERSIDAD\EDD\Usuarios.csv")
print arbol.grafica
