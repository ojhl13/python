import re
def buscar_palabra(palabra, archivo):
    with open(archivo, 'r') as f:
        texto = f.read()
        if re.search(palabra, texto):
            print('La palabra {} está en el archivo {}'.format(palabra, archivo))
        else:
            print('La palabra {} no está en el archivo {}'.format(palabra, archivo))
if __name__ == '__main__':
    buscar_palabra('version', 'input.txt')