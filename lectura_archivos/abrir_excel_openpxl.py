import openpyxl


from tkinter import filedialog


filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("all files",
                                                        "*.*"),
                                                       ("all files",
                                                        "*.*")))
#print(filename)




doc = openpyxl.load_workbook(filename)
sheets = doc.get_sheet_names()
print(sheets)