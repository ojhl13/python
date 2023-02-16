import ctypes
import win32api
import os
import winsound
import tkinter as tk
import time
from takepicturelib import *



x=win32api.GetCursorPos()[0]
xnew= 0
key=''

while(1):
	
   newx=win32api.GetCursorPos()[0]
   if win32api.GetAsyncKeyState(ord('Z')) == (-32768) :
      print('listo desactivadp')
      quit()
   if(x!= newx) or win32api.GetAsyncKeyState(ord('n')) == (-32768) :
      #text.insert('end', 'Buen intento jaja pero te gane ')z
      #os.startfile('c:\\nelson.mp3')
      #os.startfile('c:\\descarga.jpg')

      print('adios')
      takepicture()
      time.sleep(2)
      ctypes.windll.user32.LockWorkStation()
      quit()
      #ya troleaste alguein
   