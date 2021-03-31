from nodoMatriz import nodoMatriz

class listaMatrices:
    def __init__(self, inicio = None):
        self.inicio = inicio
    
    def insertarMatriz(self, nombre, filas, columnas):
        nueva = nodoMatriz(nombre, filas, columnas)
        if self.inicio is None:
            self.inicio = nueva
        else:
            tmp = self.inicio
            while tmp.siguiente is not None:
                tmp = tmp.siguiente
            tmp.siguiente = nueva
    
    def getMatriz(self, nombre):
        tmp = self.inicio
        while tmp is not None:
            if str.lower(tmp.nombre) == str.lower(nombre):
                return tmp
            tmp = tmp.siguiente
        return None
    
    def mostrar(self):
        tmp = self.inicio
        while tmp is not None:
            print("Nombre:", tmp.nombre)
            tmp.matrix.recorrerFilas()
            tmp = tmp.siguiente
