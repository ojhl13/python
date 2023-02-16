from pynput import keyboard
import os
horas = os.path.normcase(r'C:\Users\UIF21362\OneDrive - Continental AG\horas\horas2023.xlsm')
github= os.path.normcase(r'C:\Users\UIF21362\AppData\Local\GitHubDesktop\GitHubDesktop.exe')
gitbash= os.path.normcase(r'C:\Program Files\Git\git-bash.exe')
passSafe= os.path.normcase(r'C:\Program Files\Password Safe\pwsafe.exe')
#definimos las funciones que se ejecutarán en la detección



def abrir_horas():
    print('abrir excel')
    os.startfile(horas)
    
def abrir_gitbash():
    print('abrir git-bash')
    os.startfile(gitbash)
    
def abrir_github():
    print('abrir github')
    os.startfile(github)
    
def abrir_passsafe():
    print('abrirpassafe')
    os.startfile(passSafe)

def play():
    print('play')
    
def cerrar():
    exit()
	 
#definimos un diccionario con cada combinación de teclas y la función asociada
hotkeys = { 
            '<ctrl>+<alt>+<shift>+h': abrir_horas,
            '<ctrl>+<alt>+<shift>+b': abrir_gitbash,
            '<ctrl>+<alt>+<shift>+g': abrir_github,
            '<ctrl>+<alt>+<shift>+c': abrir_passsafe,
            '<ctrl>+<alt>+<shift>+<': cerrar,
            '<ctrl>+<alt>+<shift>+p': play
          }


    
if __name__ == '__main__':
#finalmente lanzamos el escuchador con la clase GlobalHotKeys
    with keyboard.GlobalHotKeys(hotkeys) as escuchador:
        escuchador.join()