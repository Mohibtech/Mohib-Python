import sys
import csv
import unicodedata
 
# Removing Diacritics from Arabic words
def remove_accents(input_str):
    nkfd_form = unicodedata.normalize('NFKD', input_str)
    ### unicodedata.combining(c) will return true if the character c can be combined with the preceding character ###
    ### that is mainly if it's a diacritic. ###
    return u"".join([c for c in nkfd_form if not unicodedata.combining(c)])
 
 
filename = r'C:\Test\Misc\Arabicwords.txt'
 
#ArabicWAccent = []
 
def load_file(filename):
    with open(filename,'r',encoding='utf8') as f:
        read = csv.reader(f)
        # Reading rows from file , Columns from rows and then applying function on word to remove Accents
        return [remove_accents(col)  for row in read for col in row]
    #return simplewords
 
ArabicWAccent = load_file(filename)
                   
for word in ArabicWAccent:
    print(word)
