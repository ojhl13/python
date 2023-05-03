from xlrd import open_workbook
from tkinter import filedialog

filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("all files",
                                                        "*.*"),
                                                       ("all files",
                                                        "*.*")))
wb = open_workbook(filename)
sheet = wb.sheet_by_index(0)
sheet.cell_value(0, 0)
columns = []
print("Columns")
 
for i in range(sheet.ncols):
    columns.append(sheet.cell_value(0, i))
    
print(columns)