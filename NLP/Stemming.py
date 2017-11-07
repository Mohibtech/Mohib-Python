# Microsoft: DAT263x Intro to AI

import os

# Load and print text
#!curl https://raw.githubusercontent.com/MicrosoftLearning/AI-Introduction/master/files/KennedyInaugural.txt -o KennedyInaugural.txt
baseDir = r'H:\Backup\Python\notebooks\Text and Speech'
doc4 = open(os.path.join(baseDir,"KennedyInaugural.txt"), "r")
kenTxt = doc4.read()

print(kenTxt)

# Normalize and remove stop words
from string import punctuation
import nltk
nltk.download("stopwords")
from nltk.corpus import stopwords

kenTxt = ''.join(c for c in kenTxt if not c.isdigit())
kenTxt = ''.join(c for c in kenTxt if c not in punctuation).lower()
kenTxt = ' '.join([word for word in kenTxt.split(' ') if word not in (stopwords.words('english'))])

# Get Frequency distribution
import pandas as pd
from nltk.probability import FreqDist

words = nltk.tokenize.word_tokenize(kenTxt)
fdist = FreqDist(words)
count_frame = pd.DataFrame(fdist, index =[0]).T
count_frame.columns = ['Count']

# Plot frequency
import matplotlib.pyplot as plt

counts = count_frame.sort_values('Count', ascending = False)
fig = plt.figure(figsize=(16, 9))
ax = fig.gca()    
counts['Count'][:60].plot(kind = 'bar', ax = ax)
ax.set_title('Frequency of the most common words')
ax.set_ylabel('Frequency of word')
ax.set_xlabel('Word')
plt.show()
