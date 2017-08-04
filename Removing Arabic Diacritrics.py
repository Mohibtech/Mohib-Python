import sys 
import csv
import unicodedata

def remove_accents(input_str):
    nkfd_form = unicodedata.normalize('NFKD', input_str)
    return u"".join([c for c in nkfd_form if not unicodedata.combining(c)])


filename = r'C:\Test\Misc\Arabicwords.txt'

with open(filename,'r',encoding='utf8') as f:
    read = csv.reader(f)
    for row in read:
        for element in row:
            print(element)
            print( remove_accents(element) )
