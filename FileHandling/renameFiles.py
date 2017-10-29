import os

workFolder = r'C:\MEDIA\TV Seasons\Walking dead'
fileList = os.listdir(workFolder)
os.chdir( workFolder )

for filename in fileList:
    fname, ext = os.path.splitext(filename)
    seasonEp = fname.split('.')
    newname = str(seasonEp[3] + '_' + seasonEp[1] + seasonEp[2] + ext)
    
    os.rename(filename, newname)
