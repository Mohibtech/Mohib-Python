```python
import re
import string
#from nltk.tokenize import RegexpTokenizer

urdu_punctuations = '''`÷×؛<>_()*&^%][ـ،/:"؟.,۔'{}~¦+|!”…“–ـ'''
eng_punctuations = string.punctuation
punctuations_list = urdu_punctuations + eng_punctuations

# Just using four characters, can include more characters from arabic to remove zair , zabar, paish etc
urdu_diacritics = re.compile("""
                            ،    | # sakta
                            ۔    | # dash
                            !    | # exclamation
                            ؛    | # semi colon
                         """, re.VERBOSE)

def remove_diacritics(text):
    text = re.sub(urdu_diacritics, '', text)
    return text

def remove_punctuations(text):
    translator = str.maketrans('', '', punctuations_list)
    return text.translate(translator)

def file_list(FILE_NAME):
    try:
        with open(FILE_NAME,'r',encoding='utf8') as textfile:
            words = textfile.read()
    except ValueError as e:
            print(e)
    return words

#text = file_list(r'urdu/Firdoos_s.txt')
text = '''معمولی تناسب ہر شخص کو بے تاب و بے قرار کر دینے کے لیے کافی ہے۔
کس نے کہا تھا اور کس سے کہا تھا، اب تو ثابت ہے اور رہنا ہے یہ ثابت!'''

text_imp = remove_punctuations(text)
#text_imp = remove_diacritics(text)

print(text_imp)
```

Another method for removing punctuations using all unicode points for punctuations

```python
def remove_unicode_punct(text):
    remove_punct_map = dict.fromkeys(i for i in range(sys.maxunicode) 
                                       if unicodedata.category(chr(i)).startswith('P'))
    return text.translate(remove_punct_map)
```


