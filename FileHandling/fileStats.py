import nltk
import string
import re
import sys
import unicodedata
import time
from collections import Counter

def word_populate(FILE_NAME):
    with open(FILE_NAME,'r',encoding='utf8') as set_file:
        bookwords = set(line.strip() for line in set_file.readlines())
    return bookwords

def file_list(FILE_NAME):
    try:
        with open(FILE_NAME,'r',encoding='utf8') as textfile:
            words = textfile.read()
    except ValueError as e:
            print(e)
    return words

def remove_punct(text):
    remove_punc_map = dict.fromkeys(i for i in range(sys.maxunicode) 
                                       if unicodedata.category(chr(i)).startswith('P'))
    return text.translate(remove_punc_map)

urdu_punctuations = '''`÷×؛<>_()*&^%][ـ،/:"؟.,۔'{}~¦+|!”…“–ـ'''
eng_punctuations = string.punctuation
punctuations_list = urdu_punctuations + eng_punctuations

# Time Starts now
t0 = time.time()

# https://github.com/Mohibtech/Mohib-Python/NLP/Firdos-e-BareeN - Abdul Haleem Sharar.txt
text = file_list(r'urdu/Firdoos.txt')

# Calling function to remove punctuations using unicode codepoints starting with 'P'
text = remove_punct(text)

#Tokenize text for sentences and words
words = nltk.word_tokenize(text)

stopwords_ur = word_populate(r'urdu/stopwords_UR.txt')

stopwords_removed = [w for w in words if w not in stopwords_ur]


# Counting num of words using Counter collection and summing up all 
words_count = Counter( stopwords_removed )
num_words = sum(words_count.values())

word_stats = [(value, key) for key, value in words_count.items()]
word_stats.sort(reverse=True)

# Counting occurences of Top 30 words
for i, (count, word) in enumerate(word_stats[:30], 1):
    print('{:>2}. {:>4} {}'.format(i, count, word))

# Ending Timer and printing total time
t1 = time.time()
total = t1-t0
print(f"Total time is {total}")
