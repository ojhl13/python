from pynput import keyboard
import os
miarchivo = os.path.normcase(r'C:\Users\UIF21362\OneDrive - Continental AG\horas\horas2023.xlsm')


#definimos las funciones que se ejecutarán en la detección



def abrir_horas():
    print('abrir excel')
    os.startfile(miarchivo)

def play():
    print('play')
	 
#definimos un diccionario con cada combinación de teclas y la función asociada
hotkeys = { 
            '<ctrl>+<alt>+<shift>+h': abrir_horas,
            '<ctrl>+<alt>+<shift>+p': play
          }


    
if __name__ == '__main__':
#finalmente lanzamos el escuchador con la clase GlobalHotKeys
    with keyboard.GlobalHotKeys(hotkeys) as escuchador:
        escuchador.join()