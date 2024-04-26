from xlrd import open_workbook

from tkinter import filedialog


filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("all files",
                                                        "*.*"),
                                                       ("all files",
                                                        "*.*")))
#print(filename)


wb = open_workbook(filename,on_demand= True)
print(wb.sheet_names())

sheet = wb.sheet_by_index(2)
sheet.cell_value(0, 0)

print(sheet.nrows)
for i in range(sheet.nrows):
    for j in range(sheet.ncols):
        print(sheet.cell_value(i, j), end = ", ")
    print()
    print(i)
    input("enter to new line")
        