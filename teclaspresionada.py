from pynput import keyboard
import os
miarchivo = os.path.normcase(r'C:\Users\UIF21362\OneDrive - Continental AG\horas\horas2023.xlsm')


#definimos las funciones que se ejecutarán en la detección
def presiona_ctrl_q():
    print('Se ha pulsado <ctrl>+q')

def presiona_alt_c():
    print('Se ha pulsado <alt>+c')

def presiona_ctrl_alt_s():
    print('Se ha pulsado <ctrl>+<alt>+s')

def abrir_horas():
    print('abrir excel')
    os.startfile(miarchivo)
	 
#definimos un diccionario con cada combinación de teclas y la función asociada
hotkeys = { '<ctrl>+q': presiona_ctrl_q,
			'<alt>+c': presiona_alt_c,
			'<ctrl>+<alt>+s': presiona_ctrl_alt_s,
			'<ctrl>+<alt>+<shift>+h': abrir_horas
            }

#finalmente lanzamos el escuchador con la clase GlobalHotKeys
with keyboard.GlobalHotKeys(hotkeys) as escuchador:
    escuchador.join()