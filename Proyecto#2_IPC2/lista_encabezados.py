from nodos import nodoEncabezado, nodoCelda

class listaEncabezado:
    def __init__(self, inicio = None):
        self.inicio = inicio

    def insertarEncabezado(self, nuevo):
        if self.inicio is None:
            self.inicio = nuevo
        elif nuevo.indice < self.inicio.indice:
            nuevo.siguiente = self.inicio
            self.inicio.anterior = nuevo
            self.inicio = nuevo
        else:
            tmp = self.inicio
            while tmp.siguiente is not None:
                if nuevo.indice < tmp.siguiente.indice:
                    nuevo.siguiente = tmp.siguiente
                    tmp.siguiente.anterior = nuevo
                    nuevo.anterior = tmp
                    tmp.siguiente = nuevo
                    break
                tmp = tmp.siguiente
            if tmp.siguiente is None:
                tmp.siguiente = nuevo
                nuevo.anterior = tmp

    def getEncabezado(self, indice):
        tmp = self.inicio
        while tmp is not None:
            if tmp.indice == indice:
                return tmp
            tmp = tmp.siguiente
        return None