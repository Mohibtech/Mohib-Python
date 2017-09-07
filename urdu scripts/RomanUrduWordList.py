import csv
import os

basedir = os.path.join("C:",os.sep,"BACKUPS","Python","urdu","data")
input_file = os.path.join(basedir,"WordListInd.csv")
out_file = os.path.join(basedir,"wordLists","output_")
logfile = os.path.join(basedir,"log_words.txt")

def csv_dict(ifile):
    with open(ifile,'r',encoding='utf-8') as f:
        d = dict(filter(None, csv.reader(f)))
    return d

def write_csvfile(wordDict, char):
    csv_ofile = out_file + char + ".csv"
    with open(csv_ofile, 'w',encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile, delimiter=',', lineterminator= '\n')
        for k,v in wordDict.items():            
            writer.writerow([k,v])

def dict_word(rom_urdu, char):
    word_dict = {k:v for k,v in rom_urdu.items() if k.startswith(char) }
    return word_dict

def write_allfiles():
    stats_list = []
    for char in alphabets:
        w_dict = dict_word(rom_urdu, char)
        print("Total words in dict {} are {}".format(char, len(w_dict)) )
        stats_list.append()
        write_csvfile(w_dict, char)
    
# Getting all characters starting from a to z
alphabets = list(map(chr, range(97, 123)))

rom_urdu = csv_dict(input_file)

write_allfiles()
print(len(rom_urdu))

