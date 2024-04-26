import tkinter
from tkinter import filedialog



def modificar_dato(ruta, filas, nuevo_dato):
    contenido = list()
    with open(ruta, 'r+') as archivo:
        contenido = archivo.readlines()
        l= len(contenido[filas-1])
        contenido[filas-1] = contenido[filas-1].rstrip('\n') +nuevo_dato + '\n'
    
    print (contenido[filas-1])
    with open(ruta, 'w') as archivo:
        archivo.writelines(contenido)
        
def leer_data(ruta):
    contenido = list()
    contador = 0
    with open(ruta, 'r+') as archivo:
        contenido = archivo.readlines()
    for linea in contenido:    
        print(str(contador)+"->"+linea)
        contador = contador + 1
    


root = tkinter.Tk()
root.withdraw()
filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("all files",
                                                        "*.*"),
                                                       ("Txt files",
                                                        "*.txt")))
                                                        

#print(filename)
#dato = str(input("ingresa dato: "))
linea2modified= int(input("linea a modificar: "))
modificar_dato(filename,linea2modified,'dey')
#leer_data(filename)