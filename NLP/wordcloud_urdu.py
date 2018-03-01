# -*- coding: utf-8 -*-
import nltk
import sys
import unicodedata
import matplotlib.pyplot as plt
from wordcloud import WordCloud

def word_populate(FILE_NAME):
    try:
        with open(FILE_NAME,'r',encoding='utf8') as set_file:
            bookwords = set(line.strip() for line in set_file.readlines())
    except ValueError as e:
           print(e)
    return bookwords

def remove_punct(text):
    remove_punc_map = dict.fromkeys(i for i in range(sys.maxunicode) 
                                       if unicodedata.category(chr(i)).startswith('P'))
    return text.translate(remove_punc_map)

def remove_stopwords(words):
    stopwords_ur = word_populate(r'urdu/stopwords_UR.txt')
    stopwords_removed = [w for w in words if w not in stopwords_ur]
    return " ".join(stopwords_removed)

# Read whole unicode text 
text = open('urdu/Firdoos.txt','r',encoding='utf8').read()

# Calling function to remove punctuations using unicode codepoints starting with 'P'
text = remove_punct(text)

# Tokenizing text into words
words = nltk.word_tokenize(text)

text = remove_stopwords(words)

# Reconstruct Arabic/Urdu sentences to be used in applications that don't support Arabic script.
from arabic_reshaper import arabic_reshaper
text = arabic_reshaper.reshape(text)

# For right-to-left text rendering, need to use get_display from python-bidi
from bidi.algorithm import get_display
text = get_display(arabic_reshaper.reshape(text))

# Generate a word cloud image
wordcloud =  WordCloud(font_path='urdu-najd-regular-1.ttf').generate(text)

# Display the generated image: the matplotlib way
import matplotlib.pyplot as plt

#matplotlib.rc('font', family='Tahoma')
plt.imshow(wordcloud.recolor(random_state=2017))
plt.title('Most Frequent Words')
plt.axis("off")
plt.show()
