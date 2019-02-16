import os
import tkinter as tk
from tkinter import filedialog

tkroot = tk.Tk()  # Initializing Tkinter
workingDir = filedialog.askdirectory(parent=tkroot,initialdir="/",title='Please select a directory')
#workingDir = r'F:\TV MEDIA\Dirilis Ertugrul\Season 2'
secondsplit = 'Big'
fileList = os.listdir(workingDir)

# Traverse root directory, and list directories as dirs and files as files
for root, dirs, fileList in os.walk(workingDir):
    os.chdir( root )
    path = root.split(os.sep)
    print((len(path) - 1) * '..', os.path.basename(root))
    
    for filename in fileList:
        fname, ext = os.path.splitext(filename)
        # First split based on char '-' or '.' , storing the first element in this cas
        if '-' in fname:
            fileSplit1 = fname.split('-')[1]
            mainName = fileSplit1.split(secondsplit)[0] #main file name
            newname = mainName.strip() + ext
            print(len(path) * '..', newname)
            os.rename(filename, newname)
        elif '.' in fname:
            fileSplit1 = fname.split('.')[1]
            mainName = fileSplit1.split(secondsplit)[0] #main file name
            newname = mainName.strip() + ext
            print(len(path) * '..', newname)
            #os.rename(filename, newname)
        else:
            print(f'Could not find Characters "-" or "." in {filename}')
