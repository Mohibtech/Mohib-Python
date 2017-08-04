# like ۱ ، ب ، ت
Urdu Dictionary of Lists of Words starting with a particular Alphabet
import os
import sys

#Function to populate a set with file contents
def list_populate(FILE_NAME):
    try:
        with open(FILE_NAME,'r',encoding='utf8') as set_file:
            lughatwords = set(line.strip() for line in set_file.readlines())
    except ValueError as e:
           print(e)
    return lughatwords

def wordList(LUGHAT,i,letter,key,dictAlfaaz={}):
    for word in LUGHAT:
        if word.startswith(letter):
            dictAlfaaz[key].append(word)
    return dictAlfaaz

urduLetters = {
"Alif":"ا","AlifMada":"آ", "Bay":"ب", "Pay":"پ", "Tay":"ت","Ttay":"ٹ","Say":"ث","Jeem":"ج",
"Chay":"چ","Hay":"ح","Khay":"خ","Daal":"د","Ddaal":"ڈ","Zaal":"ذ","Ray":"ر","Array":"ڑ","Zay":"ز","Yaal":"ژ",
"Seen":"س","Sheen":"ش","Swaad":"ص","Zwaad":"ض","Touay":"ط","Zouay":"ظ","Ain":"ع","Ghain":"غ","Fay":"ف",
"Kaaf":"ک","Qaaf":"ق","Gaaf":"گ","Laam":"ل","Meem":"م","Noon":"ن","Wow":"و","Hai":"ہ","Hamza":"ء","ChotiYay":"ی","BariYay":"ے"
}


basedir = r'C:\Test\Data'
FILE_NAME = os.path.join(basedir,"FullWords.txt")
a
LUGHAT = list_populate(FILE_NAME)

#Creating Dictionary with Urdu Letters as Keys and words starting with that letter as a list
dictWordsList = dict((k,list()) for k in urduLetters.keys())

totWords = 0
for key in urduLetters.keys():
    dictWordsList = wordList(LUGHAT,totWords,urduLetters[key],key,dictWordsList)
    print("Words in {} are: {}".format(key, len(dictWordsList[key])))
    totWords +=len(dictWordsList[key])


print("Total words are {}".format(totWords))
