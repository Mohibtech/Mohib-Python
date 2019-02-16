import nltk 

data = {}
dirpath = r'C:\TECHNICAL\Programming\Python\BOOK_CODE\Mastering_Python_for_DS\Data\madmax_review'
data['bbc'] = open('./madmax_review/bbc.txt','r').read()
data['forbes'] = open('./madmax_review/forbes.txt','r').read()
data['guardian'] = open('./madmax_review/guardian.txt','r').read()
data['moviepilot'] = open('./madmax_review/moviepilot.txt','r').read()

# We'll convert the text to lower case 
for k in data.keys():
   data[k] = data[k].lower()

print (data['bbc'][:800])