from win32api import GetKeyState
import win32api
import time


special_keys = [0x01, 0x02, 0x10,0x11,0x12, 0x20,0x25,0x26,0x27,0x28]

special = {0x01: 'leftClick',
           0x02: 'rightClick',
           0x10: 'shift',
           0x11: 'ctrl',
           0x12: 'alt',
           0x20: 'space',
           0x25: 'arrowleft',
           0x26: 'arrowup',
           0x27: 'arrowrigth',
           0x28: 'arowdown',
           }


time.sleep(1)
while True:
    for i in range(1, 256):
        if win32api.GetAsyncKeyState(i):
            if i in special_keys:
                print(special[i])
            else:
                print(hex(i))
    time.sleep(0.01)