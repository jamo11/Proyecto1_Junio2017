import matriz
class nodoJuego():
    def __init__(self, oponente, tirosr, tirosa, tirosf, bandera, dano):
        self.oponente = oponente
        self.tirosr = tirosr
        self.tirosa = tirosa
        self.tirosf = tirosf
        self.bandera = bandera
        self.dano = dano
        self.nodoSiguiente = None
        self.nodoAnterior = None

class listaJuegos():
    def __init__(self):
        self.cabeza = None
        self.graph = "digraph g{"

    def insertarJuego(self, oponente, tirosr, tirosa, tirosf, bandera, dano):
        nuevoNodo = nodoJuego(oponente, tirosr, tirosa, tirosf, bandera, dano)
        if self.cabeza is None:
            nuevoNodo.nodoSiguiente = nuevoNodo
            nuevoNodo.nodoAnterior = nuevoNodo
            self.cabeza = nuevoNodo
        else:
            nodoAux = self.cabeza.nodoAnterior
            nodoAux.nodoSiguiente = nuevoNodo
            nuevoNodo.nodoSiguiente = self.cabeza
            nuevoNodo.nodoAnterior = nodoAux
            self.cabeza.nodoAnterior = nuevoNodo

    def recorrerLista(self, usuario):
        if self.cabeza is not None:
            nodo = self.cabeza
            i = 1
            cadena = ""
            while nodo.nodoSiguiente != self.cabeza:
                cadena = cadena + '"' + usuario + str(i) + '" [label = "' + str(nodo.oponente) + ', ' + str(nodo.tirosr) + ', ' + str(nodo.dano) + '"];'
                i = i + 1
                nodo = nodo.nodoSiguiente
            cadena = cadena + '"' + usuario + str(i) + '" [label = "' + str(nodo.oponente) + ', ' + str(
                nodo.tirosr) + ', ' + str(nodo.dano) + '"];'
            nodo = 1
            for i in range(i-1):
                cadena = cadena + '"' + usuario + str(nodo) + '"->"' + usuario + str(nodo + 1) + '";'
                cadena = cadena + '"' + usuario + str(nodo + 1) + '"->"' + usuario + str(nodo) + '";'
                nodo = nodo + 1
            self.graph = self.graph + cadena + "}"
            print "self.graph: " + self.graph
            print "cadena: " + cadena
            return cadena

    def ejecutar(self):
        import os
        dotPath = "dot"
        fileInputPath = "lista.txt"
        fileOutputPath = "lista.png"
        tParam = " -Tpng "
        tOParam = " -o "
        tuple = (dotPath + tParam + fileInputPath + tOParam + fileOutputPath)
        os.system(tuple)

    def crearArch(self):
        arch = open('lista.txt', 'w')
        arch.write(str(juegos.graph))
        arch.close()

juegos = listaJuegos()
