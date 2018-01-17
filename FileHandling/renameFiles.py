import os
import tkinter as tk
from tkinter import filedialog

tkroot = tk.Tk()  # Initializing Tkinter
workingDir = filedialog.askdirectory(parent=tkroot,initialdir="/",title='Please select a directory')
#workingDir = r'F:\TV MEDIA\Dirilis Ertugrul\Season 2'
dramaSeries = " Diris Ertugrul"

fileList = os.listdir(workingDir)
os.chdir( workingDir )

# Traverse root directory, and list directories as dirs and files as files
for root, dirs, fileList in os.walk(workingDir):
    os.chdir( root )
    path = root.split(os.sep)
    print((len(path) - 1) * '..', os.path.basename(root))
    for filename in fileList:
        fname, ext = os.path.splitext(filename)
        fileSplit = fname.split('-')
        #numFileName = len(filePart)
        if len(fileSplit) > 1:
            filePart = str(fileSplit[1]).split(' ')
            newname = str(filePart[8] + " Episode" + dramaSeries + ext)
            print(len(path) * '..', newname)    
            os.rename(filename, newname)
        else:
            print(fname, len(fileSplit))



    
    
        

