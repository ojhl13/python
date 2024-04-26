import time

import openpyxl
from xlrd import open_workbook
import pandas


from tkinter import filedialog


filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("all files",
                                                        "*.*"),
                                                       ("all files",
                                                        "*.*")))
#print(filename)

inicio = time.time()
print("openpyxl")
doc = openpyxl.load_workbook(filename)
fin = time.time()
print(str(fin-inicio))

inicio = time.time()
print("xlrd on demand")
wb = open_workbook(filename,on_demand= True)
fin = time.time()
print(str(fin-inicio))

inicio = time.time()
print("xlrd")
wb = open_workbook(filename)
fin = time.time()
print(str(fin-inicio))


inicio = time.time()
print("pandas")
df = pandas.read_excel(filename)
fin = time.time()
print(str(fin-inicio))

