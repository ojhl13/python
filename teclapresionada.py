import Tkinter as tk

def onKeyPress(event):
    print('You pressed %s\n' % (event.char, ))
root = tk.Tk()

root.bind('<KeyPress>', onKeyPress)
root.mainloop()
