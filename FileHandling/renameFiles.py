import os

workFolder = r'E:\TECH VID\Oracle 12c\Oracle 12c New Features\2 ILM'
fileList = os.listdir(workFolder)
os.chdir( workFolder )

for filename in fileList:
    fname, ext = os.path.splitext(filename)
    fileNamePt = fname.split('-')
    numFileName = len(fileNamePt)
    if numFileName > 1:
        newname = str(fileNamePt[1] + ext)
        print(newname)
    else:
        print(fname, numFileName)
