import pandas
from tkinter import filedialog


filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("all files",
                                                        "*.*"),
                                                       ("all files",
                                                        "*.*")))
#print(filename)

df = pandas.read_excel(filename)
print("Columns")
print(df.columns)

'''
df = pandas.read_excel(filename)
count = 3

for index, row in df.iterrows():
    print(row, end = "\n\n")
    
    if index == count - 1:
        break
'''
