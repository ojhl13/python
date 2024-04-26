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
sheet = doc["Guidelines"]
files=[]
for col in sheet.iter_cols(min_row=3,max_col=1,values_only=True):
    for data in col:
        #print(data)
        if data not in files:
            files.append(data)
counter=0           
for data in files:
    print(data,end='\n')
    counter+=1
print (counter)