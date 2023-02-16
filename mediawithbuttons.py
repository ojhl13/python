import win32api
import time

from subprocess import call

key=''

def cicle():
   while 1:
      if(win32api.GetAsyncKeyState(0x11)):
         if(win32api.GetAsyncKeyState(0x10)):
            if(win32api.GetAsyncKeyState(0x12)):
               if(win32api.GetAsyncKeyState(0x25)):
                  print ("previous")
                  call(["python", "media_with_params.py","-pso"])
                  time.sleep(0.02)
               if(win32api.GetAsyncKeyState(0x27)):
                  print ("next")
                  call(["python", "media_with_params.py","-nso"])
                  time.sleep(0.02)
               if(win32api.GetAsyncKeyState(0x26)):
                  print ("up")
                  call(["python", "media_with_params.py","-vup"])                  
                  call(["python", "media_with_params.py","-vup"])
                  call(["python", "media_with_params.py","-vup"])
                  time.sleep(0.002)
               if(win32api.GetAsyncKeyState(0x28)):
                  print ("down")
                  call(["python", "media_with_params.py","-vdo"])
                  time.sleep(0.002)
                  call(["python", "media_with_params.py","-vdo"])
                  time.sleep(0.002)
                  call(["python", "media_with_params.py","-vdo"])
                  time.sleep(0.002)

               if(win32api.GetAsyncKeyState(ord('Q'))):
                  print ("play/pause")
                  call(["python", "media_with_params.py","-p"])
                  time.sleep(0.02)
               if(win32api.GetAsyncKeyState(ord('Z'))):
                  print ("bye")
                  exit()
              







cicle()
