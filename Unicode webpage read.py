#Unicode webpage read		
from urllib.request import urlopen
 
# Copy all of the content from UrduWeb page
URL = 'https://raw.githubusercontent.com/Mohibtech/urdu-stopwords/master/urdu_stopwords.txt'

webpage = urlopen(URL)
stopwords_UR = webpage.read().decode("utf-8")

for i,word in enumerate(stopwords_UR.split()):
    print(i,word)
