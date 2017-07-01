
class nodoEncabezado:
    def __init__(self, indice):
        self.indice = indice
        self.siguiente = None
        self.anterior = None
        self.primero = None
        self.izquierda = None
        self.arriba = None

class nodoDato:
    def __init__(self, col, fila, dato, dimension):
        self.izquierda = None
        self.derecha = None
        self.arriba = None
        self.abajo = None
        self.frente = None
        self.atras = None
        self.col = col
        self.fila = fila
        self.dato = dato
        self.dimension = dimension

class matriz:
    def __init__(self):
        self.pFila = None
        self.pCol = None
        self.grafica = 'digraph g{ rankdir = TB; node [shape = rectangle]; graph [nodesep = 0.5];'

    def insertar(self, col, fila, dato, dimension):
        nuevo = nodoDato(col, fila, dato, dimension)
        if self.pCol is None:
            self.pCol = nodoEncabezado(col)
            self.pFila = nodoEncabezado(fila)
            self.pCol.primero = nuevo
            nuevo.arriba = self.pCol
            self.pFila.primero = nuevo
            nuevo.izquierda = self.pFila
        else:
            cabezaFila = self.pFila
            while cabezaFila is not None:
                if cabezaFila.indice != fila:
                    if cabezaFila.indice < fila:
                        if cabezaFila.siguiente is None:
                            # crea encabezado nuevo al final de las filas existentes
                            aux = nodoEncabezado(fila)
                            aux.anterior = cabezaFila
                            cabezaFila.siguiente = aux
                            aux.primero = nuevo
                            nuevo.izquierda = aux
                            cabezaFila = None
                        else:
                            cabezaFila = cabezaFila.siguiente
                    elif cabezaFila.indice > fila:
                        # crea encabezado nuevo en medio de dos existentes
                        if cabezaFila == self.pFila:
                            aux = nodoEncabezado(fila)
                            self.pFila.anterior = aux
                            aux.siguiente = self.pFila
                            aux.primero = nuevo
                            nuevo.izquierda = aux
                            self.pFila = aux
                            cabezaFila = None
                        else:
                            aux = nodoEncabezado(fila)
                            nodoAnterior = cabezaFila.anterior
                            nodoAnterior.siguiente = aux
                            aux.anterior = nodoAnterior
                            aux.siguiente = cabezaFila
                            cabezaFila.anterior = aux
                            nuevo.izquierda = aux
                            aux.primero = nuevo
                            cabezaFila = None
                else:
                    nodo = cabezaFila.primero
                    bandera = True
                    while bandera:
                        columna = nodo
                        if columna.col < col:
                            if nodo.derecha is None:
                                nodo.derecha = nuevo
                                nuevo.izquierda = nodo
                                cabezaFila = None
                                bandera = False
                            else:
                                nodo = nodo.derecha
                        elif columna.col > col:
                            if nodo == cabezaFila.primero:
                                cabezaFila.primero.izquierda = nuevo
                                nuevo.derecha = cabezaFila.primero
                                nuevo.izquierda = cabezaFila
                                cabezaFila.primero = nuevo
                                cabezaFila = None
                                bandera = False
                            else:
                                prev = nodo.izquierda
                                prev.derecha = nuevo
                                nuevo.izquierda = prev
                                nuevo.derecha = nodo
                                nodo.izquierda = nuevo
                                cabezaFila = None
                                bandera = False
                        else:
                            bandera = False
                            cabezaFila = None
            # BUSCA COLUMNA A LA QUE PERTENECE EL NUEVO NODO
            cabezaCol = self.pCol
            while cabezaCol is not None:
                if cabezaCol.indice != col:
                    if cabezaCol.indice < col:
                        if cabezaCol.siguiente is None:
                            # crea encabezado nuevo al final de las filas existentes
                            aux = nodoEncabezado(col)
                            aux.anterior = cabezaCol
                            cabezaCol.siguiente = aux
                            aux.primero = nuevo
                            nuevo.arriba = aux
                            cabezaCol = aux.siguiente
                        else:
                            cabezaCol = cabezaCol.siguiente
                    elif cabezaCol.indice > col:
                        # crea encabezado nuevo en medio de dos existentes
                        if cabezaCol == self.pCol:
                            aux = nodoEncabezado(col)
                            self.pCol.anterior = aux
                            aux.siguiente = self.pCol
                            aux.primero = nuevo
                            nuevo.arriba = aux
                            self.pCol = aux
                            cabezaCol = None
                        else:
                            aux = nodoEncabezado(col)
                            nodoAnterior = cabezaCol.anterior
                            nodoAnterior.siguiente = aux
                            aux.anterior = nodoAnterior
                            aux.siguiente = cabezaCol
                            cabezaCol.anterior = aux
                            nuevo.arriba = aux
                            aux.primero = nuevo
                            cabezaCol = None
                else:
                    # LA COLUMNA ES IGUAL A UNA YA EXISTENTE
                    nodo = cabezaCol.primero
                    bandera = True
                    while bandera:
                        row = nodo
                        #while row.izquierda is not None:
                         #   row = row.izquierda
                        if row.fila < fila:
                            if nodo.abajo is None:
                                nodo.abajo = nuevo
                                nuevo.arriba = nodo
                                cabezaCol = None
                                bandera = False
                            else:
                                nodo = nodo.abajo
                        elif row.fila > fila:
                            if nodo == cabezaCol.primero:
                                nodo.arriba = nuevo
                                nuevo.abajo = nodo
                                nuevo.arriba = cabezaCol
                                cabezaCol.primero = nuevo
                                cabezaCol = None
                                bandera = False
                            else:
                                prev = nodo.arriba
                                prev.abajo = nuevo
                                nuevo.arriba = prev
                                nuevo.abajo = nodo
                                nodo.arriba = nuevo
                                cabezaCol = None
                                bandera = False
                        elif row.fila == fila:
                            self.insertarProfundidad(nodo, nuevo)
                            bandera = False
                            cabezaCol = None

    def insertarProfundidad(self, nodo, nuevo):
        bandera = True
        aux = nodo
        while bandera:
            if aux.dimension > nuevo.dimension:
                if aux.atras is None:
                    aux.atras = nuevo
                    nuevo.frente = aux
                    print "nodo" + aux.dato + " atras es: " + nuevo.dato
                    bandera = False
                else:
                    if aux.atras.dimension < nuevo.dimension:
                        nuevo.frente = aux
                        nuevo.atras = aux.atras
                        aux.atras.frente = nuevo
                        aux.atras = nuevo
                        print "nodo" + aux.dato + " atras es: " + nuevo.dato
                        bandera = False
                    else:
                        aux = aux.atras
            elif aux.dimension < nuevo.dimension:
                if aux.frente is None:
                    aux.frente = nuevo
                    nuevo.atras = aux
                    print "nodo" + str(aux.dato) + " frente es: " + str(nuevo.dato)
                    bandera = False
                else:
                    if aux.frente.dimension > nuevo.dimension:
                        nuevo.atras = aux
                        nuevo.frente = aux.frente
                        aux.frente.atras = nuevo
                        aux.frente = nuevo
                        print "nodo" + str(aux.dato) + " frente es: " + str(nuevo.dato)
                        bandera = False
                    else:
                        aux = aux.frente
            else:
                print "Ya existe el nodo"
                bandera = False


    def recorrerMatriz(self):
        fila = self.pFila
        col = self.pCol
        texto = self.grafica
        txt = ""
        if fila is not None:
            if fila.siguiente is not None:
                while fila.siguiente is not None:
                    txt = '{rank = same; "' + str(fila.indice) + '" '
                    texto = texto + '"' + str(fila.indice) + '"->"' + str(fila.siguiente.indice) + '" [dir=both];'
                    nodo = fila.primero
                    texto = texto + '"' + str(fila.indice) + '"->"' + str(nodo.dato) + '" [dir = both];'
                    txt = txt + '"' + str(nodo.dato) + '" '
                    if nodo.derecha is not None:
                        while nodo.derecha is not None:
                            texto = texto + '"' + str(nodo.dato) + '"->"' + str(nodo.derecha.dato) + '" [dir = both];'
                            txt = txt + '"' + str(nodo.derecha.dato) + '" '
                            if (nodo.atras is not None) or (nodo.frente is not None):
                                if nodo.atras is not None:
                                    aux = nodo
                                    while aux.atras is not None:
                                        texto = texto + '"' + str(aux.dato) + '"->"' + str(aux.atras.dato) + '" [dir=both];'
                                        aux = aux.atras
                                if nodo.frente is not None:
                                    aux = nodo
                                    while aux.frente is not None:
                                        texto = texto + '"' + str(aux.dato) + '"->"' + str(aux.frente.dato) + '" [dir=both];'
                                        aux = aux.frente
                            nodo = nodo.derecha
                        if (nodo.atras is not None) or (nodo.frente is not None):
                            if nodo.atras is not None:
                                aux = nodo
                                while aux.atras is not None:
                                    texto = texto + '"' + str(aux.dato) + '"->"' + str(aux.atras.dato) + '" [dir=both];'
                                    aux = aux.atras
                            if nodo.frente is not None:
                                aux = nodo
                                while aux.frente is not None:
                                    texto = texto + '"' + str(aux.dato) + '"->"' + str(
                                        aux.frente.dato) + '" [dir=both];'
                                    aux = aux.frente
                        txt = txt + "}"
                        texto = texto +  txt
                        fila = fila.siguiente
                    else:
                        texto = texto + txt + "}"
                        fila = fila.siguiente
                txt = '{rank = same; "' + str(fila.indice) + '" '
                nodo = fila.primero
                texto = texto + '"' + str(fila.indice) + '"->"' + str(nodo.dato) + '" [dir = both];'
                txt = txt + '"' + str(nodo.dato) + '" '
                if nodo.derecha is not None:
                    while nodo.derecha is not None:
                        texto = texto + '"' + str(nodo.dato) + '"->"' + str(nodo.derecha.dato) + '" [dir = both];'
                        txt = txt + '"' + str(nodo.derecha.dato) + '" '
                        nodo = nodo.derecha
                    txt = txt + "}"
                    texto = texto + txt
                else:
                    texto = texto + txt + "}"
        txt = "{rank = same; "
        if col is not None:
            txt = txt + '"' + str(col.indice) + '" '
            if col.siguiente is not None:
                while col.siguiente is not None:
                    texto = texto + '"' + str(col.indice) + '"->"' + str(col.siguiente.indice) + '" [dir=both];'
                    nodo = col.primero
                    texto = texto + '"' + str(col.indice) + '"->"' + str(nodo.dato) + '" [dir = both];'
                    txt = txt + '"' + str(col.siguiente.indice) + '" '
                    if nodo.abajo is not None:
                        while nodo.abajo is not None:
                            texto = texto + '"' + str(nodo.dato) + '"->"' + str(nodo.abajo.dato) + '" [dir = both];'
                            nodo = nodo.abajo
                        col = col.siguiente
                    else:
                        texto = texto + txt + "}"
                        col = col.siguiente
                nodo = col.primero
                texto = texto + '"' + str(col.indice) + '"->"' + str(nodo.dato) + '" [dir = both];'
                if nodo.abajo is not None:
                    while nodo.abajo is not None:
                        texto = texto + '"' + str(nodo.dato) + '"->"' + str(nodo.abajo.dato) + '" [dir = both];'
                        nodo = nodo.abajo
                else:
                    texto = texto + txt + "}"
        texto = texto + txt + "}}"
        print texto
        self.grafica = texto

    def ejecutar(self):
        import os
        dotPath = "dot"
        fileInputPath = "matriz.txt"
        fileOutputPath = "matriz.png"
        tParam = " -Tpng "
        tOParam = " -o "
        tuple = (dotPath + tParam + fileInputPath + tOParam + fileOutputPath)
        os.system(tuple)

    def crearArch(self):
        arch = open('matriz.txt', 'w')
        arch.write(str(matriz.grafica))
        arch.close()

matriz = matriz()
matriz.insertar("B", 1, "b1", 1)
matriz.insertar("B", 12, "b2", 1)
matriz.insertar("A", 15, "b3", 1)
matriz.insertar("D", 12, "b4", 1)
matriz.insertar("F", 2, "b5", 1)
matriz.insertar("D", 1, "sa6", 4)
matriz.insertar("A", 2, "b7", 1)
matriz.insertar("Z", 5, "b8", 1)
matriz.insertar("B", 2, "s9", 1)
matriz.insertar("B", 2, "a10", 3)
matriz.insertar("B", 2, "b11", 2)
matriz.insertar("D", 1, "a12", 3)
matriz.insertar("D", 1, "s13", 1)
matriz.insertar("D", 1, "b14", 2)
print "____________________________"
matriz.recorrerMatriz()
matriz.crearArch()
matriz.ejecutar()
print "____________________________"
