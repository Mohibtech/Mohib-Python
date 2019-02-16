import os
dirpath = r'C:\TECHNICAL\Programming\Python\BOOK_CODE\Mastering_Python_for_DS\Data\madmax_review'
bbcfile = dirpath + r'\bbc.txt'
forbesfile = dirpath + r'\forbes.txt'
guardianfile = dirpath + r'\guardian.txt'
moviepilotfile = dirpath + r'\moviepilot.txt'

data = {}

with open(bbcfile,encoding='utf8') as fbbc,open(forbesfile,encoding='utf8') as fforbes, \
     open(guardianfile,encoding='utf8') as fguardian, open(moviepilotfile,encoding='utf8') as fmovie:
    data['bbc'] = fbbc.read()
    data['forbes'] = fforbes.read()
    data['guardian'] = fguardian.read()
    data['moviepilot'] = fmovie.read()

#data['bbc'] = open(os.path.join(dirpath, 'bbc.txt'),'r').read()

print(data['bbc'][:80])

print(data['forbes'][:80])

print(data['guardian'][:80])

print(data['moviepilot'][:80])
