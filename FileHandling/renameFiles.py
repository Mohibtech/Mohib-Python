import os
import tkinter as tk
from tkinter import filedialog

# Initializing tkinter
root = tk.Tk()
workingDir = filedialog.askdirectory(parent=root,initialdir="/",title='Please select a directory')

fileList = os.listdir(workingDir)
os.chdir( workingDir )

for filename in fileList:
    fname, ext = os.path.splitext(filename)
    fileNamePt = fname.split('-')
    numFileName = len(fileNamePt)
    if numFileName > 1:
        newname = str(fileNamePt[1].strip() + ext)
        print(newname)
        os.rename(filename, newname)
    else:
        print(fname, numFileName)
