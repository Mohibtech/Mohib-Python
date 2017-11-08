import os 
import nltk
import matplotlib.pyplot as plt
import pandas as pd
from nltk.probability import FreqDist
nltk.download("stopwords")
from nltk.corpus import stopwords

baseDir = r'H:\Backup\Python\notebooks\Text and Speech'
# iwr -URI https://raw.githubusercontent.com/MicrosoftLearning/AI-Introduction/master/file s/Moon.txt -Outfile Moon.txt
doc1 = open(os.path.join(baseDir,'Moon.txt'), 'r')
doc1Txt = doc1.read()

# Filter out the stop words, punctuations and digits
from string import punctuation
txt = ''.join(c for c in doc1Txt if not c.isdigit())
txt = ''.join(c for c in txt if c not in punctuation).lower()
txt = ' '.join([word for word in txt.split() if word not in (stopwords.words('english'))])

# Get the frequency distribution of the remaining words
words = nltk.tokenize.word_tokenize(txt)
fdist = FreqDist(words)
count_frame = pd.DataFrame(fdist, index =[0]).T
count_frame.columns = ['Count']

# Plot the frequency of the top 60 words
counts = count_frame.sort_values('Count', ascending = False)
# Print words with counts in descending order
print( counts )

fig = plt.figure(figsize=(16, 9))
ax = fig.gca()    
counts['Count'][:60].plot(kind = 'bar', ax = ax)
ax.set_title('Frequency of the most common words')
ax.set_ylabel('Frequency of word')
ax.set_xlabel('Word')
plt.show()
