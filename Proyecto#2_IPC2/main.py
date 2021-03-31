import tkinter as tk
from tkinter import filedialog
import xml.etree.ElementTree as ET
from lista_matrices import listaMatrices
from matriz import matriz


matrices = listaMatrices()


def abrirArchivo(maestro):
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    if not file_path.endswith(".xml"):
        print("Elija un archivo valido!")
    else:
        print("")
        tree = ET.parse(file_path)
        root = tree.getroot()
        print(root.tag)
        filas = ""
        columnas = ""
        nombreM = ""
        if root.tag == "matrices":
            for elemento in root:
                nueva_matriz = matriz()
                for subelemento in elemento:
                    if subelemento.tag == "nombre":
                        nombreM = subelemento.text
                    if subelemento.tag == "filas":
                        filas = subelemento.text
                    if subelemento.tag == "columnas":
                        columnas = subelemento.text
                    if subelemento.tag == "imagen":
                        columna = 0
                        fila = 0
                        for i in range(0,len(subelemento.text)):
                            charactual = subelemento.text[i]
                            if ord(charactual) != 32:
                                if columna < int(columnas):
                                    columna += 1
                                    if charactual == "*":
                                        nueva_matriz.insertarCelda(fila,columna)
                                    #print("["+charactual, end="] ")
                                    #print("columna:",columna,"fila:",fila)
                                    if charactual == "\n":
                                        columna = 0
                                        fila += 1
                                else:
                                    columna = 0
                                    fila += 1
                print(nombreM)
                matrices.insertarMatriz(nombreM, filas, columnas)
                mprueba = matrices.getMatriz(nombreM)
                mprueba.matrix = nueva_matriz
            matrices.mostrar()
            print("")
            print("Archivo cargado exitosamente!")
            dibujarMatriz(maestro, int(filas), int(columnas))
        else:
            print("Este archivo no contiene matrices.")


def dibujarMatriz(maestro, filas, columnas):
    for i in range(filas):
        encabeF = tk.Frame(
            master=maestro,
            relief=tk.RAISED,
            borderwidth=1
            )
        encabeF.grid(row=i, column=0, padx=2, pady=2)
        rows = tk.Label(master=encabeF, text=f"F: {i}")
        rows.pack(padx=1, pady=1)
        for j in range(1,columnas):
            encabeC = tk.Frame(
                master=maestro,
                relief=tk.RAISED,
                borderwidth=1
            )
            encabeC.grid(row=0, column=j, padx=2, pady=2)
            cols = tk.Label(master=encabeC, text=f"F: {j}")
            cols.pack(padx=1, pady=1)
            frame = tk.Frame(
                master=maestro,
                relief=tk.RAISED,
                borderwidth=1
            )
            frame.grid(row=i, column=j, padx=1, pady=1)
            #print(matrices.getMatriz("M1").getCelda())
            iterMatriz = matrices.getMatriz("M3")
            nodoActual = iterMatriz.matrix
            if nodoActual.getCelda(i+1,j+1) is not None:
                label = tk.Label(master=frame, text=f"*", bg="black")
            #Row {i}\nColumn {j}
                label.pack(padx=5, pady=1)
            else:
                label = tk.Label(master=frame, text=f"-", bg ="white")
                label.pack(padx=5, pady=1)


def dibujarGUI():
    window = tk.Tk()
    window.title("Principal")
    #window.geometry("1280x720")
    window.option_add("*tearOff", False)

    window.columnconfigure(0, weight=1, minsize=1280)
    window.rowconfigure(0, weight=1, minsize=600)

    menu_bar = tk.Menu(master=window)
    window["menu"] = menu_bar

    menu_cargar = tk.Menu(menu_bar)
    menu_operaciones = tk.Menu(menu_bar)
    menu_reportes = tk.Menu(menu_bar)
    menu_ayuda = tk.Menu(menu_bar)

    menu_bar.add_cascade(menu=menu_cargar, label='Archivo')
    menu_bar.add_cascade(menu=menu_operaciones, label='Operaciones')
    menu_bar.add_cascade(menu=menu_reportes, label='Reportes')
    menu_bar.add_cascade(menu=menu_ayuda, label='Ayuda')

    principal = tk.Frame(
        master=window,
        relief=tk.FLAT,
        borderwidth=1,
    )
    principal.grid(row=1,column=0)

    menu_cargar.add_command(label='Cargar Archivo', command=abrirArchivo(principal))

    menu_operaciones.add_command(label='Rotación horizontal de una imagen')
    menu_operaciones.add_command(label='Rotación vertical de una imagen')
    menu_operaciones.add_separator()
    menu_operaciones.add_command(label='Transpuesta de una imagen')
    menu_operaciones.add_command(label='Limpiar zona de una imagen')
    menu_operaciones.add_separator()
    menu_operaciones.add_command(label='Agregar línea horizontal a una imagen')
    menu_operaciones.add_command(label='Agregar línea vertical a una imagen')
    menu_operaciones.add_separator()
    menu_operaciones.add_command(label='Agregar rectángulo')
    menu_operaciones.add_command(label='Agregar triángulo rectángulo')

    #principal = tk.Frame(
    #    master=window,
    #    relief=tk.FLAT,
    #    borderwidth=1,
    #)
    #principal.grid(row=0,column=0)

    #dibujarMatriz(principal, 3, 6)
    """label = tk.Label(
        principal,
        text="Matrices",
        width=20,
        height=5
    )
    label.grid(column=0,row=0,columnspan=2,rowspan=1)

    panel = tk.Frame(
        principal,
        width=1280,
        height=500,
        relief=tk.GROOVE,
        borderwidth=5,
        padx=25,
        pady=5,
    )
    panel.grid(column=0,row=1,columnspan=2,rowspan=1)

    grid_original = tk.Frame(panel,relief=tk.RAISED,borderwidth=1,width=600,height=250)
    grid_original.grid(column=0,row=0,columnspan=1,rowspan=1,pady=10)
    label_nombre = tk.Label(panel,text="Matriz Original")
    label_nombre.grid(column=0,row=1,columnspan=1,rowspan=1)

    grid_procesada = tk.Frame(panel,relief=tk.RAISED,borderwidth=1,width=600,height=250)
    grid_procesada.grid(column=1,row=0,columnspan=1,rowspan=1)
    label_procesada = tk.Label(panel,text="Matriz Procesada")
    label_procesada.grid(column=1,row=1,columnspan=1,rowspan=1)"""

    window.mainloop()


def main():
    dibujarGUI()

if __name__ == "__main__":
    main()


"""barraBotones = tk.Frame(bg="black")
barraBotones.pack(fill=tk.X,side=tk.TOP)

btnCargar = tk.Button(text="Cargar Archivo",master=barraBotones)
btnCargar.pack(fill=tk.X,side=tk.LEFT,expand=True)
btnOperaciones = tk.Button(text="Operaciones",master=barraBotones)
btnOperaciones.pack(fill=tk.X,side=tk.LEFT,expand=True)
btnReportes = tk.Button(text="Reportes",master=barraBotones)
btnReportes.pack(fill=tk.X,side=tk.LEFT,expand=True)
btnAyuda = tk.Button(text="Ayuda",master=barraBotones)
btnAyuda.pack(fill=tk.X,side=tk.LEFT,expand=True)


label = tk.Label(
    text="Hello, Tkinter",
    master=frame,
    width=20,
    height=10,
    bg="blue"
)
#label.place(x=15,y=10)
label.pack()

boton = tk.Button(text="boton",master=frame)
#boton.place(x=0,y=0)
boton.pack(pady=10)"""