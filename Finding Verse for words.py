#Finding a verse(شعر) from file with given words

from itertools import islice
import os

BASE = os.path.join("H:",os.sep,"MISC","URDU","NasirKazmi")
FILE = os.path.join(BASE,"Nasir.txt")

find = ('دھوپ','فراق','گرفتگی')
prevLine = ""

with open(FILE, 'r', encoding='utf-8') as infile:
    for line in infile:
            if any(word in line for word in find):
                if prevLine.strip() == '':
                    print( '{}'.format(line.rstrip()) )

                    #Print next line using islice function and value 1 for just next line
                    print( ''.join(islice(infile, 1)) )
                elif prevLine.strip() != '':
                    print(prevLine) 
                    print( line )
                    
                    #print('{:4d}: {}'.format(line_no-1, previous) )
            
            prevLine = line.lower()
