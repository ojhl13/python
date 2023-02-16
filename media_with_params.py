#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import argparse
import pyautogui

parser = argparse.ArgumentParser()
volumenvalue=0


parser.add_argument("-p", "--play", help="dar play a las canciones", action="store_true")
parser.add_argument("-vup", "--volup", help="up volumen", action="store_true")
parser.add_argument("-vdo", "--voldown", help="down volumen", action="store_true")
parser.add_argument("-vmu", "--volmute", help="mute", action="store_true")
parser.add_argument("-nso", "--nextsong", help="next song", action="store_true")
parser.add_argument("-pso", "--prevsong", help="previous song", action="store_true")
args = parser.parse_args()
 
# Aquí procesamos lo que se tiene que hacer con cada argumento
def main():
	pyautogui.press('volumedown')
	volumenvalue=int(input("escribe valor de volumen:"))

	
	print ("hola mundo")
	while(1):
		keypress=input("escribe comando\n")
		if keypress== 'z':
			exit()     	
		elif keypress[0]== 'p':
			pyautogui.press('playpause')
		elif keypress[0]== 'a':	
			for y in range(50):
				if volumenvalue < 100:
					pyautogui.press('volumeup')
					volumenvalue+=2
			#print("volumen: "+str(volumenvalue))			
		elif keypress[0]== '+':
			value=int(((int(keypress[1])*10)+(int(keypress[2]))	)/2)
			for y in range(value):
				if volumenvalue < 100:
					pyautogui.press('volumeup')
					volumenvalue+=2
			#print("volumen: "+str(volumenvalue))
		elif keypress[0]== '-':
			value=int(((int(keypress[1])*10)+(int(keypress[2])))/2)
			for y in range(value):
				if volumenvalue > 0:
					pyautogui.press('volumedown')
					volumenvalue-=2
			#print("volumen: "+str(volumenvalue))
		elif keypress[0]== 'm':
			pyautogui.press('volumemute')
		elif keypress[0]== 'n':
			pyautogui.press('nexttrack')
		elif keypress[0]== 'p':
			pyautogui.press('prevtrack')
		elif keypress[0]== 'v':
			print("volumen: "+str(volumenvalue))
		else:
			exit()

 
			

			


		
if args.play:
	print ("play o pause")
	pyautogui.press('playpause')
if args.volup:
	pyautogui.press('volumeup')
if args.voldown: 
	pyautogui.press('volumedown')
if args.volmute:
	pyautogui.press('volumemute')
if args.nextsong:
	pyautogui.press('nexttrack')
if args.prevsong:
	pyautogui.press('prevtrack')

if __name__ == '__main__':
	main()



	''' for x in range(50):
		pyautogui.press('volumedown')
		volumenvalue=volumenvalue-2
	for x in range(15):
		pyautogui.press('volumeup')
		volumenvalue=volumenvalue+2'''