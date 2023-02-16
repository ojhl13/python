'''while 1:
    tecla=raw_input()
    print(tecla)
    print(int(tecla))

print("termine")'''

import win32api
import win32con


while 1:
    tecla=input()
    #print(tecla)
    print(int(tecla))

print("termine")


while True :
    print(win32api.GetAsyncKeyState(ord('N')))
    if win32api.GetAsyncKeyState(ord('Z')) == (-32768) :
        print("done")
        break
