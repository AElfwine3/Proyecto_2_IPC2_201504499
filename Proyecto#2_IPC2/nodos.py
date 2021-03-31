class nodoEncabezado:
    def __init__(self,indice):
        self.indice = indice
        self.siguiente = None
        self.anterior = None
        self.acceso = None


class nodoCelda:
    def __init__(self, fila, columna):
        self.fila = fila
        self.columna = columna
        self.izquierda = None
        self.derecha = None
        self.arriba = None
        self.abajo = None