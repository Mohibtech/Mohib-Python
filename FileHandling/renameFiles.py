import os
import tkinter as tk
from tkinter import filedialog

tkroot = tk.Tk()  # Initializing Tkinter
workingDir = filedialog.askdirectory(parent=tkroot,initialdir="/",title='Please select a directory')
#workingDir = r'F:\TV MEDIA\Dirilis Ertugrul\Season 2'
dramaSeries = " Diris Ertugrul"
EpNum = 0

fileList = os.listdir(workingDir)

# Traverse root directory, and list directories as dirs and files as files
for root, dirs, fileList in os.walk(workingDir):
    os.chdir( root )
    path = root.split(os.sep)
    print((len(path) - 1) * '..', os.path.basename(root))
    for filename in fileList:
        fname, ext = os.path.splitext(filename)
        # First split based on char '-' , storing the first element in this case
        fileSplit1 = fname.split('-')[0]
        if len(fileSplit1) > 1:
            # second split based on empty space char " "
            EpName = fileSplit1.split(' ')
            for i in range(len(EpName)):
                # Checking every element of splitted string for a digit only to store it as the episode number
                if EpName[i].isdigit():
                    EpNum = EpName[i]

            #Episode = str(fileSplit1[0]).split(' ')
            newname = str(EpNum + dramaName + ext)
            print(len(path) * '..', newname)    
            os.rename(filename, newname)
        else:
            print(fname, len(fileSplit1))

    
    
        

