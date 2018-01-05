import os
import tkinter as tk
from tkinter import filedialog

tkroot = tk.Tk()  # Initializing Tkinter
workingDir = filedialog.askdirectory(parent=tkroot,initialdir="/",title='Please select a directory')

fileList = os.listdir(workingDir)
os.chdir( workingDir )

# Traverse root directory, and list directories as dirs and files as files
for root, dirs, fileList in os.walk(workingDir):
    path = root.split(os.sep)
    print((len(path) - 1) * '..', os.path.basename(root))
    for filename in fileList:
        fname, ext = os.path.splitext(filename)
        fileNamePt = fname.split('-')
        numFileName = len(fileNamePt)
        if numFileName > 1:
            newname = str(fileNamePt[0].strip() + ext)
            print(len(path) * '..', newname)    
            #os.rename(filename, newname)
        else:
            print(fname, numFileName)

