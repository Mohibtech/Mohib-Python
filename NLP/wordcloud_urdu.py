# -*- coding: utf-8 -*-

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
    #stopwords_ur = ['میں','اور','کو','کی','کا', 'مجھے', 'پر','اس','جب', 'مگر ', 'کر','کے','کہ','ہو','ہی','اپنی','اپنے','نہیں','ہے','ہوں','گیا','ایک','سے','پھر','کوئی','یہاں','آپ','ہیں','تک','وہاں','ہوں','میرے','ہوا','لے','تھی','گی','اگر']
    stopwords_removed = [w for w in words if w not in stopwords_ur]
    return " ".join(stopwords_removed)

# Read the whole text.
text = open('Data/Firdoos.txt','r',encoding='utf8').read()

text = remove_stopwords(text)
#text = text.decode("utf-8")
text = arabic_reshaper.reshape(text)
text = get_display(arabic_reshaper.reshape(text))

# Generate a word cloud image
wordcloud =  WordCloud(font_path='tahoma.ttf').generate(text)

#wordcloud.to_image()


# Display the generated image:
# the matplotlib way:
import matplotlib
import matplotlib.pyplot as plt

#matplotlib.rc('font', family='Tahoma')
plt.imshow(wordcloud.recolor(random_state=2017))
plt.title('Most Frequent Words')
plt.axis("off")
plt.show()
