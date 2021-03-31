from nodos import nodoCelda, nodoEncabezado
from lista_encabezados import listaEncabezado

class matriz:
    def __init__(self):
        self.encabezado_columnas = listaEncabezado()
        self.encabezado_filas = listaEncabezado()

    def insertarCelda(self, fila, columna):
        nuevo = nodoCelda(fila,columna)

        #insertar nodo con acceso de fila
        e_fila = self.encabezado_filas.getEncabezado(fila)
        if e_fila is None:
            e_fila = nodoEncabezado(fila)
            e_fila.acceso = nuevo
            self.encabezado_filas.insertarEncabezado(e_fila)
        else:
            if nuevo.columna < e_fila.acceso.columna:
                nuevo.derecha = e_fila.acceso
                e_fila.acceso.izquierda = nuevo
                e_fila.acceso = nuevo
            else:
                tmp = e_fila.acceso
                while tmp.derecha is not None:
                    if nuevo.columna < tmp.derecha.columna:
                        nuevo.derecha = tmp.derecha
                        tmp.derecha.izquierda = nuevo
                        nuevo.izquierda = tmp
                        tmp.derecha = nuevo
                        break
                    tmp = tmp.derecha
                if tmp.derecha is None:
                    tmp.derecha = nuevo
                    nuevo.izquierda = tmp
        
        #insertar nodo con acceso de columna
        e_columna = self.encabezado_columnas.getEncabezado(columna)
        if e_columna is None:
            e_columna = nodoEncabezado(columna)
            e_columna.acceso = nuevo
            self.encabezado_columnas.insertarEncabezado(e_columna)
        else:
            if nuevo.fila < e_columna.acceso.fila:
                nuevo.abajo = e_columna.acceso
                e_columna.acceso.arriba = nuevo
                e_columna.acceso = nuevo
            else:
                tmp = e_columna.acceso
                while tmp.abajo is not None:
                    if nuevo.fila < tmp.abajo.fila:
                        nuevo.abajo = tmp.abajo
                        tmp.abajo.arriba = nuevo
                        nuevo.arriba = tmp
                        tmp.abajo = nuevo
                        break
                    tmp = tmp.abajo
                if tmp.abajo is None:
                    tmp.abajo = nuevo
                    nuevo.arriba = tmp

    def recorrerFilas(self):
        e_fila = self.encabezado_filas.inicio
        print("---   Recorrido por Filas ---")
        while e_fila is not None:
            tmp = e_fila.acceso
            print("Fila:", str(tmp.fila))
            print("Columna")
            while tmp is not None:
                print(str(tmp.columna))
                tmp = tmp.derecha
            e_fila = e_fila.siguiente
        print("---   Fin   ---")
    
    def getCelda(self, fila, columna):
        e_fila = self.encabezado_filas.inicio
        while e_fila is not None:
            tmp = e_fila.acceso
            if tmp.fila == fila:
                while tmp is not None:
                    if tmp.columna == columna:
                        return tmp
                    tmp = tmp.derecha
            e_fila = e_fila.siguiente
        return None

    def recorrerColumnas(self):
        e_columna = self.encabezado_columnas.inicio
        print("---   Recorrido por Columnas ---")
        while e_columna is not None:
            tmp = e_columna.acceso
            print("Columna:", str(tmp.columna))
            print("Fila")
            while tmp is not None:
                print(str(tmp.fila))
                tmp = tmp.abajo
            e_columna = e_columna.siguiente
        print("---   Fin   ---")


#m = matriz("probando")
#m.insertarCelda(2,5)
#m.insertarCelda(0,6)
#m.insertarCelda(4,2)
#m.insertarCelda(2,1)
#m.insertarCelda(0,8)
#m.insertarCelda(4,3)
#m.recorrerFilas()
#m.recorrerColumnas()