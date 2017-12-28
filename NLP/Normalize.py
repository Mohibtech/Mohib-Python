import os
import nltk
nltk.download("stopwords")
from nltk.corpus import stopwords


baseDir = r'H:\Backup\Python\notebooks\Text and Speech'

# Get first document, normalize it, and remove stop words
#iwr -URI https://raw.githubusercontent.com/MicrosoftLearning/AI-Introduction/master/files/Moon.txt -Outfile Moon.txt
doc1 = open(os.path.join(baseDir,'Moon.txt'), 'r')
doc1Txt = doc1.read()
print (doc1Txt)

from string import punctuation
txt1 = ''.join(c for c in doc1Txt if not c.isdigit())
txt1 = ''.join(c for c in txt1 if c not in punctuation).lower()
txt1 = ' '.join([word for word in txt1.split() if word not in (stopwords.words('english'))])

# Get a second document, normalize it, and remove stop words
#iwr -URI https://raw.githubusercontent.com/MicrosoftLearning/AI-Introduction/master/files/Gettysburg.txt -Outfile Gettysburg.txt
print("------------------------------------------------")
doc2 = open(os.path.join(baseDir,'Gettysburg.txt'), 'r')
doc2Txt = doc2.read()
print (doc2Txt)

#from string import punctuation
txt2 = ''.join(c for c in doc2Txt if not c.isdigit())
txt2 = ''.join(c for c in txt2 if c not in punctuation).lower()
txt2 = ' '.join([word for word in txt2.split() if word not in (stopwords.words('english'))])

# and a third
#!curl https://raw.githubusercontent.com/MicrosoftLearning/AI-Introduction/master/files/Cognitive.txt -o Cognitive.txt
print("------------------------------------------------")

doc3 = open(os.path.join(baseDir,'Cognitive.txt'), 'r')
doc3Txt = doc3.read()
print (doc3Txt)

#from string import punctuation
txt3 = ''.join(c for c in doc3Txt if not c.isdigit())
txt3 = ''.join(c for c in txt3 if c not in punctuation).lower()
txt3 = ' '.join([word for word in txt3.split() if word not in (stopwords.words('english'))])

# install textblob library and define functions for TF-IDF
# !pip install -U textblob
import math
from textblob import TextBlob as tb

def tf(word, doc):
    return doc.words.count(word) / len(doc.words)

def contains(word, docs):
    return sum(1 for doc in docs if word in doc.words)

def idf(word, docs):
    return math.log(len(docs) / (1 + contains(word, docs)))

def tfidf(word, doc, docs):
    return tf(word,doc) * idf(word, docs)


# Create a collection of documents as textblobs
doc1 = tb(txt1)
doc2 = tb(txt2)
doc3 = tb(txt3)
docs = [doc1, doc2, doc3]

# Use TF-IDF to get the three most important words from each document
print('-----------------------------------------------------------')
for i, doc in enumerate(docs):
    print("Top words in document {}".format(i + 1))
    scores = {word: tfidf(word, doc, docs) for word in doc.words}
    sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    for word, score in sorted_words[:3]:
        print("\tWord: {}, TF-IDF: {}".format(word, round(score, 5)))
