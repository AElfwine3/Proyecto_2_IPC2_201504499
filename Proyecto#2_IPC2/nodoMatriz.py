from matriz import matriz


class nodoMatriz:
    def __init__(self,nombre, filas, columnas):
        self.nombre = nombre
        self.filas = filas
        self.columnas = columnas
        self.matrix = matriz()
        self.siguiente = None