
from xlrd import open_workbook
from tkinter import filedialog


filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("all files",
                                                        "*.*"),
                                                       ("all files",
                                                        "*.*")))
#print(filename)
wb = open_workbook(filename)
sheet2use =input("write the number of the sheet starting to 0") 
sheet = wb.sheet_by_index(2)
#print (sheet)
cell =sheet.cell_value(1, 0)
print(str(cell))
columns = ["0"]
print("Columns")
count = 0


for i in range(sheet.ncols):
    columns.append(str(i)+"->"+str(sheet.cell_value(1, i)))
    print(str(i)+"->"+str(sheet.cell_value(1, i)))
    columns.append(sheet.cell_value(1, i))
