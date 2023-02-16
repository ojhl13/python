from pynput import keyboard as kb

def pulsa(tecla):
	print('Se ha pulsado la tecla ' + str(tecla))

with kb.Listener(pulsa) as escuchador:
	escuchador.join()