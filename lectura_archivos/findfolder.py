import tkinter
from tkinter import filedialog
root = tkinter.Tk()
root.withdraw()
dirname = filedialog.askdirectory(parent=root,initialdir="/",title='Please select a directory')
print(dirname)