from tkinter import *

ws = Tk()

ws.geometry('500x500')
ws.title("Python Guides")

def call():
    text = text_edit.get(0.3,END)
    print(text)

text_edit = Text(ws, width=56, height=25)

text_edit.pack()

ws.mainloop()