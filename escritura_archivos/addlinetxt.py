import tkinter
from tkinter import filedialog



def modificar_dato(filename, match, content):
    contenido = list()
    lines = open(filename).read().splitlines()
    index = lines.index('a')
    lines.insert(int(match), content)
    open(filename, mode='w').write('\n'.join(lines))
        
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
#leer_data()
linea2modified= int(input("linea a modificar: "))
modificar_dato(filename,linea2modified,"dey")
#leer_data(filename)