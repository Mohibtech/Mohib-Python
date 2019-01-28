'''
Load a file from github using requests library
'''
import requests

github_file = 'https://raw.githubusercontent.com/Mohibtech/urdu-stopwords/master/urdu_stopwords.txt'
urdustopwords = requests.get(github_file)

stopwords = urdustopwords.text.split()
for text in stopwords:
    print(text)
