import re

archivo = "input.txt"
salida = "result.txt"
busqueda = 'version'
lineas_escribir = []
with open(archivo, "r") as archivo_lectura:
    numero_linea = 0
    for linea in archivo_lectura:
        numero_linea += 1
        linea = linea.rstrip()
        separado = linea.split(" ")
        if busqueda in separado:
            out=re.findall(r"(?:'.*?')|(?:\".*?\")", linea)
            string1= str(out).split(".")
            print(string1)
            lineas_escribir.append(str(string1))
with open(salida, "w") as archivo_salida:
    for linea in lineas_escribir:
        archivo_salida.write(linea + "\n")