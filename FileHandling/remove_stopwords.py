from wordcloud import WordCloud
import nltk
import matplotlib.pyplot as plt
from arabic_reshaper import arabic_reshaper
from bidi.algorithm import get_display

def word_populate(FILE_NAME):
    try:
        with open(FILE_NAME,'r',encoding='utf8') as set_file:
            bookwords = set(line.strip() for line in set_file.readlines())
    except ValueError as e:
           print(e)
    return bookwords

def remove_stopwords(text):
    words = nltk.word_tokenize(text)
    stopwords_ur = word_populate(r'urdu/stopwords_UR.txt')
    stopwords_removed = [w for w in words if w not in stopwords_ur]
    return " ".join(stopwords_removed)

# Read the whole text.
text = open('urdu/Firdoos_s.txt','r',encoding='utf8').read()

text = remove_stopwords(text)

print(text)
