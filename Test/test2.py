import os
from tkinter import Tk, Label, Entry, StringVar
from tkinter import filedialog

app = Tk()

def findfile(start, name):
    for relpath, dirs, files in os.walk(start):
        if name in files:
            full_path = os.path.join(start, relpath, name)
            print(os.path.normpath(os.path.abspath(full_path)))
 

labelText=StringVar()
labelText.set("Directory Selected")
labelDir=Label(app, textvariable=labelText, height=4)
#labelDir.pack(side="left")
labelDir.grid(row=1,column=1)

folder_selected = filedialog.askdirectory()

labelText=StringVar()
labelText.set(folder_selected)
labelDir=Label(app, textvariable=labelText, height=4)
#labelDir.pack(side="left")
labelDir.grid(row=1,column=2)

# Label for File input
labelText=StringVar()
labelText.set("Enter File Name")
labelDir=Label(app, textvariable=labelText, height=4)
labelDir.grid(row=2,column=1)

directory=StringVar(None)
dirname=Entry(app,textvariable=folder_selected,width=50)
#dirname.pack(side="left")
dirname.grid(row=2,column=2)
result = dirname.get()

print(result)

app.mainloop()